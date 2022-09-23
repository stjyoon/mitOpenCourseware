public class fooCorp{
    public static double calculatePay(double pay, int hours){
        double totalPay = 0;
        if (hours > 40){
            totalPay = pay*1.5*(hours-40)+(pay*40);
            }
        else {
            totalPay = pay*hours;
        }
        return totalPay;
    }
    public static void main(String[] args){
        double e1 = calculatePay(7.50, 35);
        double e2 = calculatePay(8.20, 47);
        double e3 = calculatePay(10.00,73);
        System.out.println("Employee one gets "+e1);
        System.out.println("Employee 2 gets "+e2);
        System.out.println("Employee 3 gets "+ e3);
    }
}
