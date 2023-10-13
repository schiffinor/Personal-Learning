/*
Never finished implementing this machine learning system. It should work, I wasn't too far from finishing the
implementation I just needed to put the random action selector and implement the reward function.
 */
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;
import java.util.regex.*;

/**
 * @author      Roman Schiffino <rjschi24@colby.edu>
 * @version     1.1
 * @since       1.1
 */
public class glipper {
    FileWriter fileWriter;

    public glipper() throws IOException {
        fileWriter = new FileWriter("combined.txt");
        BufferedReader fileGetter = null;
        // AZMAIN, N'wah from Morrowind, ADJUST THIS FOR FILE COUNT. J<101 MEANS 100 FILES 1.txt-100.txt.
        for (int j = 1; j < 4; j++) {
            fileGetter = new BufferedReader(new FileReader(j + ".txt"));
            String currLine;
            do {
                currLine = fileGetter.readLine();
                if (currLine == null) break;
                currLine = currLine.toLowerCase();
                fileWriter.write(currLine + "\n");
            } while (true);
            // Close object.
            fileGetter.close();
        }
        fileWriter.close();
    }

    public static void main(String[] args) throws IOException {
        glipper glipper = new glipper();
    }
}
