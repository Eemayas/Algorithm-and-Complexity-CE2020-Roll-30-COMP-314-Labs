import java.util.Arrays;

class MergeWorstCase
{
    public static void print(int arr[])
    {
        System.out.println();
        for(int i=0;i<arr.length;i++)
            System.out.print(arr[i]+" ");
        System.out.println();
    }
    public static void merge(int[] arr, int[] left, int[] right) {
        int i,j;
        for(i=0;i<left.length;i++)
                arr[i]=left[i];
        for(j=0;j<right.length;j++,i++)
                arr[i]=right[j];
    }

    //Pass a sorted array here
    public static void seperate(int[] arr) { 

        if(arr.length<=1)
            return;
        
        if(arr.length==2)
        {
            int swap=arr[0];
            arr[0]=arr[1];
            arr[1]=swap;
            return;
        }

        int i,j;
        int m = (arr.length + 1) / 2;
        int left[] = new int[m];
        int right[] = new int[arr.length-m];

        for(i=0,j=0;i<arr.length;i=i+2,j++) //Storing alternate elements in left subarray
            left[j]=arr[i];

        for(i=1,j=0;i<arr.length;i=i+2,j++) //Storing alternate elements in right subarray
            right[j]=arr[i];

        seperate(left);
        seperate(right);
        merge(arr, left, right);
    }

    public static void create_a_worst_case_array_on_unsorted(int[] arr) {
        Arrays.sort(arr);

        seperate(arr);

    }

    public static void main(String args[])
    {
        int arr1[]={0,1,2,3,4,5,6,7};
        create_a_worst_case_array_on_unsorted(arr1);
        System.out.print("For array 1:");
        print(arr1);

        int arr2[]={0,1,2,3,4,5,6,7,8};
        create_a_worst_case_array_on_unsorted(arr2);
        System.out.print("For array 2:");
        print(arr2);     

        int arr3[]={94, 67, 15, 45, 27, 95, 89, 40, 54, 42};
        create_a_worst_case_array_on_unsorted(arr3);
        System.out.print("For array 3:");
        print(arr3);   

        int arr4[]={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};
        create_a_worst_case_array_on_unsorted(arr4);
        System.out.print("For array 4:");
        print(arr4);        
    }
}