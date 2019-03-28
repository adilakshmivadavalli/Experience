import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Formatter;
import java.util.NoSuchElementException;

public class Compare {
	
	public static int[][] compare() {
		BufferedReader hunt = null;

		// Prepare an arrayList for catch the content
		ArrayList<String> cut = new ArrayList<String>();

		// Read the .txt file by using BufferedReader
		try {
			String path = "target_data.txt";
			String temp;
			hunt = new BufferedReader(new FileReader(path));

			// Catch all the content from the .txt in ArrayList "cut"
			while ((temp = hunt.readLine()) != null) {
				cut.add(temp);
			}
		}

		catch (NoSuchElementException | IllegalStateException | IOException e) {
			System.out.println("There is something wrong.");
			System.exit(1);

		}

		// Get int m, p from "cut"
		int m = Integer.parseInt(String.valueOf((String) cut.get(0)));
		int p = cut.size() - 1;

		// Begin to create a two-dimensional arrays
		int[][] t = new int[p+1][m+1];

		// Use two for loop to insert value to the two-dimensional arrays
		for (int k = 1; k < p+1; k++) {
			for (int j = 1; j < m+1; j++) {
				String[] temp2 = cut.get(k).split(" ");
				int count = Integer.parseInt(String.valueOf(temp2[j-1]));
				t[k][j] = count * 2 - 1;
			}
		}

		// Try to output in separated files
		Formatter output;
		for (int k = 1; k < p+1; k++) {
			String inputName = "t" + k + "j.txt";
			try {
				FileOutputStream input = new FileOutputStream(inputName);
				output = new Formatter(inputName);
				for (int j = 1; j < m + 1; j++) {
					output.format("%d     %d%n", j, t[k][j]);
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
		return t;
	}
	

}
