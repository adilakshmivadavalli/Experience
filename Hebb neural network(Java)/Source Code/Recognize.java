import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.Formatter;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class Recognize {
	// Method that calculates the activation function
	static int activationFunction(int f) {
		int fy = -1;
		if (f >= 0)
			fy = 1;
		return fy;
	}

	// Method that compare the two string
	public static String compare(String a, String[] b) {

		String result = "*";
		if (b[0].equals(a)) {
			result = "A";
		} else if (b[1].equals(a)) {
			result = "B";
		} else if (b[2].equals(a)) {
			result = "C";
		} else if (b[3].equals(a)) {
			result = "D";
		}
		else if (b[4].equals(a)) {
			result = "E";
		} else if (b[5].equals(a)) {
			result = "F";
		} else if (b[6].equals(a)) {
			result = "G";
		} else if (b[7].equals(a)) {
			result = "H";
		} else if (b[8].equals(a)) {
			result = "I";
		} else if (b[9].equals(a)) {
			result = "J";
		} else if (b[10].equals(a)) {
			result = "K";
		} else if (b[11].equals(a)) {
			result = "L";
		} else if (b[12].equals(a)) {
			result = "M";
		} else if (b[13].equals(a)) {
			result = "N";
		} else if (b[14].equals(a)) {
			result = "O";
		} else if (b[15].equals(a)) {
			result = "P";
		} else if (b[16].equals(a)) {
			result = "Q";
		} else if (b[17].equals(a)) {
			result = "R";
		} else if (b[18].equals(a)) {
			result = "S";
		} else if (b[19].equals(a)) {
			result = "T";
		} else if (b[20].equals(a)) {
			result = "U";
		} else if (b[21].equals(a)) {
			result = "V";
		} else if (b[22].equals(a)) {
			result = "W";
		} else if (b[23].equals(a)) {
			result = "X";
		} else if (b[24].equals(a)) {
			result = "Y";
		} else if (b[25].equals(a)) {
			result = "Z";
		} else if (b[26].equals(a)) {
			result = "a";
		} else if (b[27].equals(a)) {
			result = "b";
		} else if (b[28].equals(a)) {
			result = "c";
		} else if (b[29].equals(a)) {
			result = "d";
		} else if (b[30].equals(a)) {
			result = "e";
		} else if (b[31].equals(a)) {
			result = "f";
		} else if (b[32].equals(a)) {
			result = "g";
		} else if (b[33].equals(a)) {
			result = "h";
		} else if (b[34].equals(a)) {
			result = "i";
		} else if (b[35].equals(a)) {
			result = "j";
		} else if (b[36].equals(a)) {
			result = "k";
		} else if (b[37].equals(a)) {
			result = "l";
		} else if (b[38].equals(a)) {
			result = "m";
		} else if (b[39].equals(a)) {
			result = "n";
		} else if (b[40].equals(a)) {
			result = "o";
		} else if (b[41].equals(a)) {
			result = "p";
		} else if (b[42].equals(a)) {
			result = "q";
		} else if (b[43].equals(a)) {
			result = "r";
		} else if (b[44].equals(a)) {
			result = "s";
		} else if (b[45].equals(a)) {
			result = "t";
		} else if (b[46].equals(a)) {
			result = "u";
		} else if (b[47].equals(a)) {
			result = "v";
		} else if (b[48].equals(a)) {
			result = "w";
		} else if (b[49].equals(a)) {
			result = "x";
		} else if (b[50].equals(a)) {
			result = "y";
		} else if (b[51].equals(a)) {
			result = "z";
		}
		return result;
	}

	// Method that get y_out.txt by using test_data.txt
	public static void Recognize() {
		// Use the method to get two-dimensional arrays
		int[][] w = getW.getFileW();
		int[][] T = Compare.compare();
		int[][] S = Training.train();

		String take;
		String whole = "";
		String pattern = "";
		String RC = "";

		// Read the .txt file by using scanner
		try (Scanner input = new Scanner(Paths.get("test_data.txt"))) {
			pattern = input.nextLine();
			RC = input.nextLine();

			// Read and catch all the String in the .txt as "whole"
			while (input.hasNext()) {

				take = input.next();
				whole = whole + take;
			}
		}
		// Catch errors
		catch (NoSuchElementException | IllegalStateException | IOException e) {
			System.exit(1);

		}

		// Split the string RC to get row and column, also get the p_test and n
		String[] rowAndColumn = RC.split(" ");
		int p_test = Integer.parseInt(String.valueOf(pattern));
		int numberOfRows = Integer.parseInt(String.valueOf(rowAndColumn[0]));
		int numberOfColumns = Integer.parseInt(String.valueOf(rowAndColumn[1]));
		int n = numberOfRows * numberOfColumns;

		// Create a String array patterns to store the patterns from
		// test_data.txt
		String[] patterns = new String[p_test];

		// When patterns count less equal 9, it will have 64 numbers for each
		for (int a = 0; a < 9; a++) {
			String cut = whole.substring((numberOfRows * numberOfColumns + 1) * a,
					(numberOfRows * numberOfColumns + 1) * (a + 1));
			patterns[a] = cut;
		}

		// When patterns count more than 9, it will have 65 numbers for each
		if (p_test > 10) {
			for (int b = 9; b < p_test; b++) {
				String cut2 = whole.substring(
						(numberOfRows * numberOfColumns + 2) * (b - 9) + (numberOfRows * numberOfColumns + 1) * 9,
						(numberOfRows * numberOfColumns + 2) * (b - 8) + (numberOfRows * numberOfColumns + 1) * 9);
				patterns[b] = cut2;
			}
		}

		// Create the new the two-dimensional arrays S_new
		int[][] S_new = new int[p_test + 1][n + 1];

		// Use two for loop to insert value to the two-dimensional arrays
		for (int k = 1; k < p_test + 1; k++) {
			for (int i = 1; i < n + 1; i++) {
				char[] temp = patterns[k - 1].toCharArray();
				S_new[k][i] = Character.digit(temp[i - 1], 10) * 2 - 1;
			}
		}

		int m = 0;
		m = T[m].length - 1;

		// p_test is the number of test patterns
		int y_in;
		int y[][] = new int[p_test + 1][m + 1];

		// Initialize outputs y
		for (int k = 0; k < p_test + 1; k++) {
			for (int j = 0; j < m + 1; j++) {
				y[k][j] = 0;
			}
		}

		// Calculate the bipolar outputs, Loop over all the test patterns
		for (int k = 1; k < p_test + 1; k++) {
			for (int j = 1; j < m + 1; j++) {
				y_in = 0;
				for (int i = 1; i < n + 1; i++) {
					int xi = S_new[k][i];
					y_in = y_in + xi * w[i][j];
				}
				y[k][j] = activationFunction(y_in);
			}
		}

		// Combine all the number from y[][] as a String
		String[] combine = new String[p_test + 1];
		for (int j = 0; j < p_test + 1; j++) {
			combine[j] = "";
		}

		for (int k = 1; k < p_test + 1; k++) {
			for (int j = 1; j < m + 1; j++) {

				combine[k] = combine[k] + y[k][j] + "  ";
			}
		}

		// for(int a=1 ;a<64;a++)
		// System.out.println(S_new[1][a]);

		// Combine all the number from T[][] as a String
		int p = S.length - 1;
		String[] combine2 = new String[p + 1];
		for (int j = 0; j < p + 1; j++) {
			combine2[j] = "";
		}
		for (int k = 0; k < p; k++) {
			for (int j = 1; j < m + 1; j++) {

				combine2[k] = combine2[k] + T[k + 1][j] + "  ";
			}
		}

		// Try to output y_out.txt

		Formatter output;
		String filename = "y_out.txt";

		try {
			FileOutputStream Y = new FileOutputStream(filename);
			output = new Formatter(filename);
			output.format("%s%n%s%n%s%n", "Data output",
					"k                   Bipolar Output                  String Output",
					"--   -------------------------------------------    -------------");
			for (int k = 1; k < p_test + 1; k++) {

				output.format("%d    %s     %s%n", k, combine[k], compare(combine[k], combine2));
			}

			// Close the formatter "output"
			output.close();

			// Try to close FileOutputStream "input"
			try {
				Y.close();
			} catch (Exception e) {
				System.out.println("There is something wrong, try again!");
			}

		} catch (FileNotFoundException e) {
			System.out.println("There is something wrong, try again!");
		}
		System.out.println("Done!");

	}
}
