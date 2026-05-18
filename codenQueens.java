public class codenQueens{
    static int count =0;
    public static void printBoard(char board[][]){
        int n = board.length;
        count++;
        System.out.println("------Board Number "+count+"--------");
        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                System.out.print(board[i][j]+" ");
            }
            System.out.println();
        }
    }
    public static void nQueens(char board[][] , int row ,boolean colUsed[] , boolean leftDiag[] , boolean rightDiag[] ){
        int n = board.length;
        //base case
        if(row == n){
            printBoard(board);
            return;
        }
        //kaam
        for(int col = 0;col<n;col++){
            int d1 = row-col +n-1;
            int d2 = row+col;
            if(!colUsed[col] && !leftDiag[d1] && !rightDiag[d2]){
                //place the queen
                board[row][col] = 'Q';
                colUsed[col] = true;
                leftDiag[d1] = true;
                rightDiag[d2] = true;
                //for next row
                nQueens(board, row+1, colUsed, leftDiag, rightDiag);
                // remove the queen
                board[row][col] = '.';
                colUsed[col] = false;
                leftDiag[d1] = false;
                rightDiag[d2] = false;
            }
        }
    }
    public static void main(String[] args) {
        int n = 5;
        char board[][]= new char[n][n];
        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                board[i][j] = '.';
            }
        }
        boolean colUsed[] = new boolean[n];
        boolean leftDiag[] = new boolean[2*n-1];
        boolean rightDiag[] = new boolean[2*n-1];
        nQueens(board , 0 , colUsed ,leftDiag , rightDiag );
    }
}