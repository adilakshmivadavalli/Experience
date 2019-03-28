import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.Formatter;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class Training {
	public static int[][] train() {
		// Read the .txt file by using scanner
				String take;
				String whole = "";
				String pattern = "";
				String RC = "";

				try (Scanner input = new Scanner(Paths.get("training_data.txt"))) {
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
					System.out.println("There is something wrong.");
					System.exit(1);

				}

				// Split the string RC to get row and column, also get the p and n
				String[] rowAndColumn = RC.split(" ");
				int p = Integer.parseInt(String.valueOf(pattern));
				int numberOfRows = Integer.parseInt(String.valueOf(rowAndColumn[0]));
				int numberOfColumns = Integer.parseInt(String.valueOf(rowAndColumn[1]));
				int n = numberOfRows * numberOfColumns;
				
				// Create a String array patterns to store the patterns from
				// test_data.txt
				String[] patterns = new String[p];

				for (int a = 0; a < p; a++) {
					String cut = whole.substring((n + 1) * a,
							(n + 1) * (a + 1));
					patterns[a] = cut;
				}

				// Begin to create a two-dimensional arrays
				int[][] s = new int[p+1][n+1];

				// Use two for loop to insert value to the two-dimensional arrays
				for (int k = 1; k < p+1; k++) {
					for (int i = 1; i < n+1; i++) {
						char[] temp = patterns[k-1].toCharArray();
						s[k][i] = Integer.parseInt(String.valueOf(temp[i-1])) * 2 - 1;
					}
				}

				// Try to output in separated files
				Formatter output;
				for (int k = 1; k < p+1; k++) {
					String inputName = "s" + k  + "i.txt";
					try {
						FileOutputStream input = new FileOutputStream(inputName);
						output = new Formatter(inputName);
						for (int i = 1; i < n + 1; i++) {
							output.format("%d     %d%n", i, s[k][i]);
						}

						// Close the formatter "output"
						output.close();

						// Try to close FileOutputStream "input"
						try {
							input.close();
						} catch (Exception e) {
							System.out.println("There is something wrong, try again!");
						}
					} catch (FileNotFoundException e) {
						System.out.println("There is something wrong, try again!");
					}

				}
		return s;
	}

}
