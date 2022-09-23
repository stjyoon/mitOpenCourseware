class Marathon {
    public static int fastest(int[] times){
        int result = 0;
        for (int i = 0; i < times.length;i++){
            if(times[i]>result){
                result = times[i];
            }
        }
        return result;
    }
    public static int secondFastest(int[] times, int fastest){
        int secondResult = 0;
        for (int i = 0; i<times.length;i++){
            if(times[i]>secondResult && times[i]<fastest){
                secondResult = times[i];
            }
        }
        return secondResult;
    }
    public static void main (String[] arguments) {
        String[] names = {
            "Elena", "Thomas", "Hamilton", "Suzie", "Phil", "Matt", "Alex",
            "Emma", "John", "James", "Jane", "Emily", "Daniel", "Neda",
            "Aaron", "Kate"
        };

        int[] times = {
            341, 273, 278, 329, 445, 402, 388, 275, 243, 334, 412, 393, 299,
            343, 317, 265
        };

        for (int i = 0; i < names.length; i++) {
            System.out.println(names[i] + ": " + times[i]);
        }
        int fastestTime = fastest(times);
        int secondFastestTime = secondFastest(times, fastestTime);
        System.out.println("the fastest time is "+ fastestTime);
        System.out.println("the second fastest time is "+secondFastestTime);
    }
}
