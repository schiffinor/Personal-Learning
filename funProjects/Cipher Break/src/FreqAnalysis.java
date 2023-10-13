import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;


public class FreqAnalysis {

    private HashMap<Integer,Integer> freqMapInput;
    private HashMap<Integer,Integer> freqMapCorp;
    private HashMap<Integer,Integer> freqMapText;


    private FreqAnalysis() throws IOException {
        BufferedReader fileGetter = null;
        freqMapInput = new HashMap<>();
        freqMapCorp = new HashMap<>();
        freqMapText = new HashMap<>();
        for (int j = 0; j < 3; j++) {
            String fileName = switch (j) {
                case 0 -> "inputCorpus.txt";
                case 1 -> "cypherCorpus.txt";
                case 2 -> "cypherText.txt";
                default -> throw new IllegalStateException("Unexpected value: " + j);
            };
            HashMap<Integer,Integer> map = switch (j) {
                case 0 -> freqMapInput;
                case 1 -> freqMapCorp;
                case 2 -> freqMapText;
                default -> throw new IllegalStateException("Unexpected value: " + j);
            };
            fileGetter = new BufferedReader(new FileReader(fileName));
            String currLine = "";
            do {
                currLine = fileGetter.readLine();
                if (currLine == null) break;
                currLine = currLine.toLowerCase();
                for (int c : currLine.toCharArray()) {
                    int value = map.getOrDefault((int) c, 0);
                    map.put(c, value + 1); ;
                }
            } while (true);
            // Close object.
            fileGetter.close();

        }
        System.out.println("Input");
        // Display values of all keys.
        for (int key : freqMapInput.keySet()) {
            System.out.println((char) key + ": " + freqMapInput.get(key));
        }
        System.out.println("CypheredInput");
        // Display values of all keys.
        for (int key : freqMapCorp.keySet()) {
            System.out.println((char)key + ": " + freqMapCorp.get(key));
        }
        System.out.println("decypher");
        // Display values of all keys.
        for (int key : freqMapText.keySet()) {
            System.out.println((char) key + ": " + freqMapText.get(key));
        }
    }

    public static void main(String[] args) throws Exception {
        FreqAnalysis freqAnalysis = new FreqAnalysis();
    }


}
