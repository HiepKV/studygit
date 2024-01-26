/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.studyclassjava;
import java.util.Scanner;
/**
 *
 * @author PC
 */
public class StudyClassJava {
    static int count = 0;
    public static void main(String[] args) {
        Studen myList[]= new Studen[50];
        int answer;
        int choice;// khoi tao bien de chon he thong
        Scanner sc = new Scanner(System.in);
        do{
            System.out.println("1.Add a student");
            System.out.println("2. Show list student");
            System.out.println("3.Find infor of Stuent by ID or Email");
            System.out.println("4. Delete infor of Studen");
            System.out.println("5. Find Student is older than x");
            System.out.println("Input your choice");
            choice = sc.nextInt();
            switch(choice){
                case 1 : System.out.println("You add a student");
                // them 1 thong tin sv
                    if(count > myList.length){System.out.println("List is full");}
                    else{
                        int Id, Age;
                        String Name, Email;
                        System.out.println("Input Id : ");
                        Id = sc.nextInt();
                        System.out.println("Input Name : ");
                        Name = sc.next();
                        System.out.println("Input Email : ");
                        Email = sc.next();
                        System.out.println("Input Age : ");
                        Age = sc.nextInt();
                        myList[count] = new Studen(Id, Age, Name, Email);
                        count++;
                    }
                break;
                case 2: System.out.println("Show the list Student");
                    for(int i = 0;i < count ;i++){
                        System.out.println(myList[i]);
                    }
                break;
                case 3: System.out.println("Find infor of Student By Id or Email");
                    int secondchoice;
                    System.out.println("1.Find by Id" );
                    System.out.println("2.Find by Email ");
                    secondchoice = sc.nextInt();
                    switch(secondchoice){
                        case 1:
                            int id;
                            System.out.println("Input Id student ou want");
                            id = sc.nextInt();
                            for(int i = 0; i < count; i++){
                                if(id == myList[i].getId()){
                                    System.out.println(myList[i]);
                                }
                            }
                            break;
                        case 2:
                            String email;
                            System.out.println("Input Email you want");
                            email = sc.next();
                            for(int i = 0; i < count; i++){
                                if(email == myList[i].getEmail()){
                                    System.out.println(myList[i]);
                                }
                            }
                            break;
                        default:
                    }
                    break;
                case 4: System.out.println("Input Income Number of student to delete");
                    int intcome;
                    intcome = sc.nextInt(); // chon so thu tu cua sinh vien trong list
                    if(intcome > 0 && intcome < 51){
                        for (int i = 0; i< count ;i++){
                            if(i == intcome - 1 ){
                                myList[i] = myList[i+1];
                                count--;
                            }
                        }
                    }
                    break;
                default:
                    
            }
            System.out.println("Do you want continue Input yes = 0 || no = different number");
            answer = sc.nextInt();
        }while(answer == 0);
    }
}
