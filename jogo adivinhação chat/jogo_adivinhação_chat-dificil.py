#!/usr/bin/env python3
"""
jogo_avancado.py
Jogo da adivinhação - versão avançada (2 jogadores, OOP, leaderboard JSON).
Roda: python jogo_avancado.py
"""
import json
import os
import random
import time
from dataclasses import dataclass, asdict
from typing import List

LEADERBOARD_FILE = "leaderboard.json"

@dataclass
class ScoreEntry:
    player: str
    score: int
    date: str  # ISO date-like simple string

class Leaderboard:
    def __init__(self, path=LEADERBOARD_FILE, max_entries=10):
        self.path = path
        self.max_entries = max_entries
        self.entries: List[ScoreEntry] = []
        self._load()

    def _load(self):
        if not os.path.exists(self.path):
            self.entries = []
            return
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                raw = json.load(f)
            self.entries = [ScoreEntry(**e) for e in raw]
        except Exception:
            self.entries = []

    def add(self, entry: ScoreEntry):
        self.entries.append(entry)
        # ordenar por score desc
        self.entries.sort(key=lambda e: e.score, reverse=True)
        self.entries = self.entries[: self.max_entries]
        self._save()

    def _save(self):
        try:
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump([asdict(e) for e in self.entries], f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def display(self):
        if not self.entries:
            print("Nenhum registro ainda no leaderboard.")
            return
        print("\n=== LEADERBOARD ===")
        for i, e in enumerate(self.entries, 1):
            print(f"{i}. {e.player:<20} {e.score:>6} pts  ({e.date})")
        print("===================\n")

class InvalidInput(Exception):
    pass

class GuessingGame:
    DIFFICULTY_SETTINGS = {
        "1": {"name": "Fácil", "limit": 50, "attempts": 10},
        "2": {"name": "Médio", "limit": 100, "attempts": 7},
        "3": {"name": "Difícil", "limit": 200, "attempts": 5},
    }

    def __init__(self, leaderboard: Leaderboard):
        self.lb = leaderboard

    def choose_difficulty(self):
        while True:
            print("Escolha o nível:")
            for k, v in self.DIFFICULTY_SETTINGS.items():
                print(f"{k} - {v['name']} (1..{v['limit']}, {v['attempts']} tentativas)")
            choice = input("Nível: ").strip()
            if choice in self.DIFFICULTY_SETTINGS:
                return self.DIFFICULTY_SETTINGS[choice]
            print("Escolha inválida. Tente novamente.\n")

    @staticmethod
    def read_player_name(prompt):
        while True:
            name = input(prompt).strip()
            if not name:
                print("Nome não pode ficar em branco.")
                continue
            return name

    @staticmethod
    def read_int(prompt):
        val = input(prompt).strip()
        if val.lower() == "sair":
            raise InvalidInput("sair")
        if not val.lstrip("-").isdigit():
            raise InvalidInput("not_int")
        return int(val)

    def compute_score(self, base: int, attempts_left: int, difference: int) -> int:
        # fórmula de pontuação: base + bônus por tentativas + penalidade por diferença
        bonus = attempts_left * 50
        penalty = difference * 2
        score = max(0, base + bonus - penalty)
        return score

    def single_round(self, setter_name: str, guesser_name: str, limit: int, attempts_allowed: int):
        # O jogador 'setter' escolhe o número secreto dentro do limite (sem mostrar)
        print(f"{setter_name}, agora você vai escolher o número secreto para {guesser_name} adivinhar.")
        while True:
            try:
                print(f"(Entrada oculta) {setter_name}, digite o número secreto entre 1 e {limit}:")
                # para evitar que o outro veja, pedimos confirmação e pausas; não dá pra ocultar no terminal sem libs
                secret = self.read_int("Número secreto: ")
                if secret < 1 or secret > limit:
                    print(f"O número deve estar entre 1 e {limit}.")
                    continue
                # limpeza de tela simples
                print("\n" * 30)
                print(f"{guesser_name}, sua vez! Tente adivinhar.\n")
                break
            except InvalidInput as e:
                if str(e) == "sair":
                    raise

        base_points = 1000
        attempts_left = attempts_allowed
        for attempt_no in range(1, attempts_allowed + 1):
            print(f"Tentativa {attempt_no}/{attempts_allowed} | Tentativas restantes: {attempts_left}")
            try:
                guess = self.read_int("Seu palpite (ou 'sair' para encerrar rodada): ")
            except InvalidInput as e:
                if str(e) == "sair":
                    print("Rodada cancelada pelo jogador.")
                    return None
                print("Entrada inválida: digite um número.")
                continue

            if guess < 1 or guess > limit:
                print(f"Número fora do intervalo 1..{limit}. Tente novamente.")
                continue

            if guess == secret:
                difference = abs(secret - guess)
                score = self.compute_score(base_points, attempts_left, difference)
                print(f"🎉 {guesser_name} acertou! Número: {secret}")
                print(f"Pontos ganhos: {score}")
                return {"winner": guesser_name, "score": score}
            else:
                difference = abs(secret - guess)
                if difference <= 3:
                    hint_prox = "🔥 Muito muito perto!"
                elif difference <= 10:
                    hint_prox = "🌡️ Perto!"
                elif difference <= 25:
                    hint_prox = "⚠️ Um pouco longe."
                else:
                    hint_prox = "❄️ Muito longe."
                direction = "MAIOR" if guess < secret else "MENOR"
                print(f"O número secreto é {direction}. {hint_prox}")
                # penalidade dinâmica
                attempts_left -= 1

        # fim das tentativas
        print(f"\nFim das tentativas! O número era {secret}.")
        # pontuação 0 para quem não acertou
        return {"winner": None, "score": 0}

    def play_two_players(self):
        print("=== MODO 2 JOGADORES ===")
        p1 = self.read_player_name("Nome do Jogador 1 (quem define o número primeiro): ")
        p2 = self.read_player_name("Nome do Jogador 2 (quem adivinha primeiro): ")

        difficulty = self.choose_difficulty()
        limit = difficulty["limit"]
        attempts = difficulty["attempts"]

        round_no = 1
        while True:
            print(f"\n--- RODADA {round_no} ---")
            # rodada: p1 define, p2 adivinha
            try:
                res = self.single_round(p1, p2, limit, attempts)
            except InvalidInput:
                print("Jogo interrompido.")
                return
            if res and res["winner"]:
                self.lb.add(ScoreEntry(player=res["winner"], score=res["score"], date=time.strftime("%Y-%m-%d %H:%M")))
            # trocar papéis
            try:
                res2 = self.single_round(p2, p1, limit, attempts)
            except InvalidInput:
                print("Jogo interrompido.")
                return
            if res2 and res2["winner"]:
                self.lb.add(ScoreEntry(player=res2["winner"], score=res2["score"], date=time.strftime("%Y-%m-%d %H:%M")))

            round_no += 1
            # mostrar leaderboard e perguntar se quer continuar
            self.lb.display()
            cont = input("Continuar jogando? (s/n): ").strip().lower()
            if cont != "s":
                print("Encerrando modo 2 jogadores.")
                break

def main():
    lb = Leaderboard()
    game = GuessingGame(lb)
    print("Bem-vindo ao Jogo de Adivinhação - Versão Avançada")
    while True:
        print("\nMenu:\n1) Jogar (2 jogadores)\n2) Ver leaderboard\n3) Sair")
        opt = input("Escolha: ").strip()
        if opt == "1":
            game.play_two_players()
        elif opt == "2":
            lb.display()
        elif opt == "3":
            print("Até a próxima!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
