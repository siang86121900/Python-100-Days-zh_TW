package org.mobiletrain;

import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Example04 {

    /**
     * 產生[min, max)範圍的隨機整數
     */
    public static int randomInt(int min, int max) {
        return (int) (Math.random() * (max - min) + min);
    }

    /**
     * 輸出一組雙色球號碼
     */
    public static void display(List<Integer> balls) {
        for (int i = 0; i < balls.size(); ++i) {
            System.out.printf("%02d ", balls.get(i));
            if (i == balls.size() - 2) {
                System.out.print("| ");
            }
        }
        System.out.println();
    }

    /**
     * 生成一組隨機號碼
     */
    public static List<Integer> generate() {
        List<Integer> redBalls = new ArrayList<>();
        for (int i = 1; i <= 33; ++i) {
            redBalls.add(i);
        }
        List<Integer> selectedBalls = new ArrayList<>();
        for (int i = 0; i < 6; ++i) {
            selectedBalls.add(redBalls.remove(randomInt(0, redBalls.size())));
        }
        Collections.sort(selectedBalls);
        selectedBalls.add(randomInt(1, 17));
        return selectedBalls;
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("機選幾注: ");
            int num = sc.nextInt();
            for (int i = 0; i < num; ++i) {
                display(generate());
            }
        }
    }
}