import java.util.Random;

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



int example4( int[] arr ){
    int sum = 0;
    for( int i = 0; i < 10; i++ ){
        for( int j = i + 1; j < 10; j++ ){
            if( arr[j] < 0 ){ return 10;}
        }
    }
    return sum;
}
// Worst Case: O(1) and Omega(1)
// Best Case: O(1) and Omega(1)


int example5( int[] arr ){
    Random rand = new Random();
    int sum = 0;
    for( int i = 0; i < 10; i++ ){
        for( int j = i + 1; j < 10; j++ ){
            if( rand.nextInt() < 20 ){ return 10;}
        }
    }
    return sum;
}
// Worst Case: O(1) and Omega(1)
// Best Case: O(1) and Omega(1)

int example6( int[] arr ){
    int sum = 0;
    for( int i = 0; i < arr.length; i++ ){
        sum++;
    }
    for( int j = 1; j < arr.length; j++ ){
        if( arr[j] < 0 ){ return 10;}
    }
    return sum;
}
// Worst Case: O(n) and Omega(n)
// Best Case: O(n) and Omega(n)


int example7( int[] arr, int find ){
    int s = 0; int e = arr.length - 1;
    while( s <= e ){
        int mid = (s + e) / 2;
        if( arr[mid] == find) return mid;
        if( arr[mid] < find ) s = mid + 1;
        else e = mid - 1;
    }
    return -1;
}
// Worst Case: O(log n) and Omega(log n)
// Best Case: O(1) and Omega(1)


