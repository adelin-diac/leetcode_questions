package easy.add_binary;

class Solution {
    // public String addBinary(String a, String b) {
    // int lenA = a.length();
    // int lenB = b.length();
    // int diff = lenA - lenB;
    // // initialise it to lenght of a -> update accordingly if b is bigger
    // int longestLen = lenA;

    // String prependedZeros = "";

    // for (int i = 0; i < Math.abs(diff); i++) {
    // prependedZeros += "0";
    // }

    // if (diff > 0) {
    // b = prependedZeros + b;
    // } else if (diff < 0) {
    // a = prependedZeros + a;
    // longestLen = b.length();
    // }

    // int charA = a.charAt(longestLen - 1) - '0';
    // int charB = b.charAt(longestLen - 1) - '0';

    // int carry = charA & charB;
    // String result = (charA ^ charB) + "";

    // for (int i = longestLen - 2; i >= 0; i--) {
    // charA = a.charAt(i) - '0';
    // charB = b.charAt(i) - '0';

    // result = (charA ^ charB ^ carry) + "" + result;
    // carry = (charA & charB) | (charA & carry) | (charB & carry);

    // }
    // if (carry == 1) {
    // result = "1" + result;
    // }

    // return result;
    // }

    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int carry = 0;
        int i = a.length() - 1;
        int j = b.length() - 1;
        while (i >= 0 || j >= 0 || carry == 1) {
            if (i >= 0) {
                carry += a.charAt(i--) - '0';
            }
            if (j >= 0) {
                carry += b.charAt(j--) - '0';
            }
            sb.append(carry % 2);
            carry /= 2;
        }
        return sb.reverse().toString();

    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.addBinary("11", "1"));
        System.out.println(s.addBinary("1010", "1011"));
        System.out.println(s.addBinary("10101", "1011"));

    }
}