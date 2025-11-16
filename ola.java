import java.io.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;

/**
 * GuessingGame.java
 * Modo 2 jogadores, menu, níveis, placar simples salvo em arquivo texto.
 *
 * Compilar: javac GuessingGame.java
 * Rodar: java GuessingGame
 */
public class GuessingGame {
    private static final String LEADERBOARD_FILE = "leaderboard.txt";
    private static final Scanner sc = new Scanner(System.in, "UTF-8");
    private static final Random rand = new Random();

    public static void main(String[] args) {
        Leaderboard lb = new Leaderboard(LEADERBOARD_FILE);
        System.out.println("Bem-vindo ao Jogo da Adivinhação (Java) - Modo Avançado");
        while (true) {  
            System.out.println("\nMenu:");
            System.out.println("1) Jogar (2 jogadores)");
            System.out.println("2) Ver leaderboard");
            System.out.println("3) Sair");
            System.out.print("Escolha: ");
            String opt = sc.nextLine().trim();
            switch (opt) {
                case "1":
                    playTwoPlayers(lb);
                    break;
                case "2":
                    lb.display();
                    break;
                case "3":
                    System.out.println("Até a próxima!");
                    return;
                default:
                    System.out.println("Opção inválida.");
            }
        }
    }

    private static void playTwoPlayers(Leaderboard lb) {
        System.out.print("Nome do Jogador 1 (quem define primeiro): ");
        String p1 = readNonEmpty();
        System.out.print("Nome do Jogador 2 (quem adivinha primeiro): ");
        String p2 = readNonEmpty();

        Difficulty diff = chooseDifficulty();
        int round = 1;
        while (true) {
            System.out.println("\n--- RODADA " + round + " ---");
            Result r1 = singleRound(p1, p2, diff);
            if (r1.winner != null) {
                lb.add(r1.winner, r1.score);
            }
            Result r2 = singleRound(p2, p1, diff);
            if (r2.winner != null) {
                lb.add(r2.winner, r2.score);
            }
            lb.display();
            System.out.print("Continuar jogando? (s/n): ");
            String c = sc.nextLine().trim().toLowerCase();
            if (!c.equals("s")) {
                break;
            }
            round++;
        }
    }

    private static Difficulty chooseDifficulty() {
        while (true) {
            System.out.println("Escolha o nível:");
            System.out.println("1 - Fácil (1 a 50, 10 tentativas)");
            System.out.println("2 - Médio (1 a 100, 7 tentativas)");
            System.out.println("3 - Difícil (1 a 200, 5 tentativas)");
            System.out.print("Nível: ");
            String opt = sc.nextLine().trim();
            switch (opt) {
                case "1": return new Difficulty(50, 10);
                case "2": return new Difficulty(100, 7);
                case "3": return new Difficulty(200, 5);
                default: System.out.println("Escolha inválida.");
            }
        }
    }

    private static Result singleRound(String setter, String guesser, Difficulty diff) {
        System.out.println(setter + ", escolha um número secreto entre 1 e " + diff.limit);
        int secret = 0;
        while (true) {
            System.out.print("Número secreto: ");
            String s = sc.nextLine().trim();
            try {
                secret = Integer.parseInt(s);
                if (secret < 1 || secret > diff.limit) {
                    System.out.println("Fora do intervalo.");
                    continue;
                }
                System.out.println("\n".repeat(20));
                System.out.println(guesser + ", é sua vez de adivinhar!");
                break;
            } catch (NumberFormatException ex) {
                System.out.println("Digite apenas números.");
            }
        }

        int base = 1000;
        int attemptsLeft = diff.attempts;
        for (int i = 1; i <= diff.attempts; i++) {
            System.out.println("Tentativa " + i + " de " + diff.attempts + " | Restam: " + attemptsLeft);
            System.out.print("Seu palpite: ");
            String s = sc.nextLine().trim();
            int guess;
            try {
                guess = Integer.parseInt(s);
            } catch (NumberFormatException ex) {
                System.out.println("Entrada inválida.");
                i--; // não conta como tentativa válida
                continue;
            }
            if (guess < 1 || guess > diff.limit) {
                System.out.println("Fora do intervalo 1.." + diff.limit);
                i--;
                continue;
            }
            if (guess == secret) {
                int diffAbs = Math.abs(secret - guess);
                int score = computeScore(base, attemptsLeft, diffAbs);
                System.out.println("🎉 " + guesser + " acertou! Número: " + secret);
                System.out.println("Pontos: " + score);
                return new Result(guesser, score);
            } else {
                int diffAbs = Math.abs(secret - guess);
                String hint;
                if (diffAbs <= 3) hint = "🔥 Muito muito perto!";
                else if (diffAbs <= 10) hint = "🌡️ Perto!";
                else if (diffAbs <= 25) hint = "⚠️ Um pouco longe.";
                else hint = "❄️ Muito longe.";
                String direction = (guess < secret) ? "MAIOR" : "MENOR";
                System.out.println("O número secreto é " + direction + ". " + hint);
                attemptsLeft--;
            }
        }
        System.out.println("Fim das tentativas. O número era: " + secret);
        return new Result(null, 0);
    }

    private static int computeScore(int base, int attemptsLeft, int difference) {
        int bonus = attemptsLeft * 50;
        int penalty = difference * 2;
        int score = Math.max(0, base + bonus - penalty);
        return score;
    }

    private static String readNonEmpty() {
        while (true) {
            String s = sc.nextLine().trim();
            if (!s.isEmpty()) return s;
            System.out.print("Nome não pode ficar em branco. Digite novamente: ");
        }
    }

    // --- Aux classes ---
    static class Difficulty {
        int limit;
        int attempts;
        Difficulty(int l, int a) { limit = l; attempts = a; }
    }

    static class Result {
        String winner;
        int score;
        Result(String w, int s) { winner = w; score = s; }
    }

    static class Leaderboard {
        private final String path;
        private final List<String> lines = new ArrayList<>();

        Leaderboard(String path) {
            this.path = path;
            load();
        }

        void load() {
            lines.clear();
            File f = new File(path);
            if (!f.exists()) return;
            try (BufferedReader br = new BufferedReader(new FileReader(f))) {
                String l;
                while ((l = br.readLine()) != null) lines.add(l);
            } catch (IOException e) {
                // ignore
            }
        }

        void add(String player, int score) {
            String time = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm"));
            String line = String.format("%s | %d pts | %s", player, score, time);
            lines.add(line);
            // ordenar por score (extrair)
            lines.sort((a, b) -> {
                try {
                    int sa = Integer.parseInt(a.split("\\|")[1].trim().split(" ")[0]);
                    int sb = Integer.parseInt(b.split("\\|")[1].trim().split(" ")[0]);
                    return Integer.compare(sb, sa);
                } catch (Exception ex) {
                    return a.compareTo(b);
                }
            });
            // manter top 10
            while (lines.size() > 10) lines.remove(lines.size() - 1);
            save();
        }

        void save() {
            try (BufferedWriter bw = new BufferedWriter(new FileWriter(path))) {
                for (String l : lines) bw.write(l + "\n");
            } catch (IOException e) {
                // ignore
            }
        }

        void display() {
            if (lines.isEmpty()) {
                System.out.println("Nenhum registro no leaderboard.");
                return;
            }
            System.out.println("\n=== LEADERBOARD ===");
            int i = 1;
            for (String l : lines) {
                System.out.println(i + ") " + l);
                i++;
            }
            System.out.println("===================\n");
        }
    }
}
