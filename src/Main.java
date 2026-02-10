void main() {
}

void example1( int[] arr ){
    int sum = 0;
    for( int i = 0; i < arr.length; i++ ){
        for( int j = i + 1; j < arr.length; j++ ){
            sum++;
        }
    }
}
// Worst Case: O(n^2) and Omega(n^2)
// Best Case: O(n^2) and Omega(n^2)



int example2( int[] arr ){
    int sum = 0;
    for( int i = 0; i < arr.length; i++ ){
        for( int j = i + 1; j < arr.length; j++ ){
            if( arr[j] < 0 ){ break;}
        }
    }
    return sum;
}
// Worst Case: O(n^2) and Omega(n^2)
// Best Case: O(n) and Omega(n)

int example3( int[] arr ){
    int sum = 0;
    for( int i = 0; i < arr.length; i++ ){
        for( int j = i + 1; j < arr.length; j++ ){
            if( arr[j] < 0 ){ return 10;}
        }
    }
    return sum;
}
// Worst Case: O(n^2) and Omega(n^2)
// Best Case: O(1) and Omega(1)

