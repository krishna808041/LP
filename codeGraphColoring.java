public class codeGraphColoring {

    /*
     * count is used to count how many valid coloring solutions are found.
     * If count remains 0, it means no solution exists.
     */
    static int count = 0;

    /*
     * This is the graph represented using Adjacency Matrix.
     *
     * Meaning:
     * graph[i][j] = 1 means vertex i and vertex j are connected.
     * graph[i][j] = 0 means vertex i and vertex j are NOT connected.
     *
     * Example:
     * graph[0][1] = 1 means vertex 0 is connected to vertex 1.
     * graph[1][3] = 0 means vertex 1 is not connected to vertex 3.
     *
     * Graph structure:
     *
     * Vertex 0 is connected to 1, 2, 3
     * Vertex 1 is connected to 0, 2
     * Vertex 2 is connected to 0, 1, 3
     * Vertex 3 is connected to 0, 2
     */
    static int graph[][] = {
            {0, 1, 1, 1},
            {1, 0, 1, 0},
            {1, 1, 0, 1},
            {1, 0, 1, 0}
    };

    /*
     * m means number of colors available.
     *
     * Here m = 3, so colors are:
     * Color 1
     * Color 2
     * Color 3
     *
     * We are checking whether this graph can be colored using 3 colors.
     */
    static int m = 3;

    /*
     * This function prints one valid coloring solution.
     *
     * color[i] stores the color assigned to vertex i.
     *
     * Example:
     * color[0] = 1 means Vertex 0 has Color 1.
     * color[1] = 2 means Vertex 1 has Color 2.
     */
    public static void printColors(int color[]) {
        count++;
        System.out.println("------Solution Number " + count + "--------");

        for (int i = 0; i < color.length; i++) {
            System.out.println("Vertex " + i + " ---> Color " + color[i]);
        }

        System.out.println();
    }

    /*
     * This function checks whether assigning color c to current vertex is safe or not.
     *
     * Rule of graph coloring:
     * Two connected vertices should not have the same color.
     *
     * Parameters:
     * vertex = current vertex we want to color
     * c      = color we want to assign
     * color  = array storing already assigned colors
     */
    public static boolean isSafe(int vertex, int c, int color[]) {
        int n = graph.length;

        /*
         * Check current vertex with every other vertex.
         */
        for (int i = 0; i < n; i++) {

            /*
             * graph[vertex][i] == 1 means current vertex is connected to vertex i.
             *
             * color[i] == c means connected vertex i already has the same color
             * that we are trying to assign to current vertex.
             *
             * If both conditions are true, then this color is not safe.
             */
            if (graph[vertex][i] == 1 && color[i] == c) {
                return false;
            }
        }

        /*
         * If no connected vertex has same color,
         * then it is safe to assign this color.
         */
        return true;
    }

    /*
     * This is the main backtracking function.
     *
     * It tries to assign colors to vertices one by one.
     *
     * vertex = current vertex number
     * color[] = stores colors assigned to vertices
     */
    public static void graphColoring(int vertex, int color[]) {
        int n = graph.length;

        /*
         * Base case:
         * If vertex == n, it means all vertices are colored successfully.
         *
         * Example:
         * If n = 4, vertices are 0, 1, 2, 3.
         * When vertex becomes 4, all vertices are done.
         */
        if (vertex == n) {
            printColors(color);
            return;
        }

        /*
         * Try every color from 1 to m for the current vertex.
         *
         * Here m = 3, so loop tries:
         * Color 1
         * Color 2
         * Color 3
         */
        for (int c = 1; c <= m; c++) {

            /*
             * Before assigning color c to current vertex,
             * check whether it is safe or not.
             */
            if (isSafe(vertex, c, color)) {

                /*
                 * If safe, assign color c to current vertex.
                 */
                color[vertex] = c;

                /*
                 * Now move to next vertex.
                 */
                graphColoring(vertex + 1, color);

                /*
                 * Backtracking step:
                 *
                 * Remove the assigned color.
                 *
                 * Why?
                 * Because after finding one solution, we want to try other possible colors
                 * and find more solutions.
                 */
                color[vertex] = 0;
            }
        }
    }

    public static void main(String[] args) {

        /*
         * n is number of vertices in the graph.
         *
         * Here graph has 4 vertices:
         * 0, 1, 2, 3
         */
        int n = graph.length;

        /*
         * color array stores color assigned to each vertex.
         *
         * Initially all values are 0.
         * 0 means no color assigned yet.
         *
         * Example:
         * color[0] = 0 means vertex 0 has no color.
         */
        int color[] = new int[n];

        /*
         * Start coloring from vertex 0.
         */
        graphColoring(0, color);

        /*
         * If no solution was printed, count will remain 0.
         */
        if (count == 0) {
            System.out.println("No solution exists");
        }
    }
}