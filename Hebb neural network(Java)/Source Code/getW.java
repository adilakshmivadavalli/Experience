import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.util.Formatter;

public class getW {

	public static int[][] getFileW() {
		// Use the method input and output, than get the return as S[][] and
		// T[][].
		int[][] S = Training.train();
		int[][] T = Compare.compare();
		int n = 0, m = 0, p = 0;

		// Get n, m and p's values from S[][] and T[][]
		n = S[n].length - 1;
		m = T[m].length - 1;
		p = S.length - 1;

		// Create the two dimension array w[ ][ ] with dimensions w[n+1][m+1]
		int[][] w = new int[n + 1][m + 1];

		// Initialize all the elements to zero in w[i][j]
		for (int i = 0; i < n + 1; i++) {
			for (int j = 0; j < m + 1; j++) {
				w[i][j] = 0;
			}
		}

		// Use three for loops to insert value to the two-dimensional arrays w
		int xi, yj, dw;
		for (int k = 1; k < p + 1; k++) {
			for (int i = 1; i < n + 1; i++) {
				for (int j = 1; j < m + 1; j++) {
					xi = S[k][i];
					yj = T[k][j];
					dw = xi * yj;
					w[i][j] = w[i][j] + dw;
				}
			}
		}

		// Save the weight matrix to file w.txt
		Formatter output;
		String filename = "w.txt";
		try {
			FileOutputStream W = new FileOutputStream(filename);
			output = new Formatter(filename);
			for (int i = 1; i < n + 1; i++) {
				for (int j = 1; j < m + 1; j++) {
					output.format("%d     %d     %d%n", i, j, w[i][j]);
				}
			}
			// Close the formatter "output"
			output.close();

			// Try to close FileOutputStream "input"
			try {
				W.close();
			} catch (Exception e) {
				System.out.println("There is something wrong, try again!");
			}

		} catch (FileNotFoundException e) {
			System.out.println("There is something wrong, try again!");
		}

		return w;

	}

}
