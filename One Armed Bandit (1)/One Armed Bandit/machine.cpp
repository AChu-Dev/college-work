#pragma once
#include "banker.h"
#include "machine.h"
#include <vector>
#include <string>
#include <cstdlib>
#include <stdlib.h>
#include <ctime>
#include <iostream>
#include <iomanip>


using namespace std;


Machine::Machine() {
	srand(time(NULL));
	cout << "Help is automatically run at the end of one activation of the system"<<endl;
	cout << "Press Enter to start the system";
	cin.get();
	attract_Mode();
	spin_Reels();

}


void Machine::attract_Mode() {
	y.Banker::jPot = 5.00;
	system("cls");
	cout << "======================================================================" << endl;
	cout << "=								     =" << endl;
	cout << "=                                   JackPot:  " << std::fixed << std::setprecision(2) << y.Banker::jPot << "		     =" << endl;
	cout << "=                                             ------------	     =" << endl;
	cout << "=      10p Per Play!!!		      Money:  " << std::fixed << std::setprecision(2) << y.Banker::curr << "      	     =" << endl;
	cout << "=                                             ------------	     =" << endl;
	cout << "=								     =" << endl;
	cout << "=               Press 3 To Spin The Reel!!!			     =" << endl;
	cout << "=								     =" << endl;
	cout << "=			  " << a << "	" << b << "		" << c << "		     =" << endl;
	cout << "=		---" << d << "		" << e << "		  " << f << "--- 		     =" << endl;
	cout << "=			  " << g << "	" << h << "		" << i << "		     =" << endl;
	cout << "=								     =" << endl;
	cout << "======================================================================" << endl;
}

void Machine::spin_Reels() {
	string reel_1[] = { "Orange", "Melon ", "   7  ", "Orange", "Orange", "   7  ", "Melon " };
	string reel_2[] = { "   7  ", "Melon ", "   7  ", "Melon ", "Melon ", "Orange", "Melon " };
	string reel_3[] = { "   7  ", "Orange", "Orange", "   7  ", "Melon ", "Melon ", "Orange" };
	reel_Act1 = 0, reel_Act2 = 0, reel_Act3 = 0, top_Row1 = 0, top_Row2 = 0, top_Row3 = 0, top_Row1_ = 0, top_Row2_ = 0, top_Row3_ = 0;
	bot_Row1 = 0, bot_Row2 = 0, bot_Row3 = 0, bot_Row1_ = 0, bot_Row2_ = 0, bot_Row3_ = 0;
	a, b, c, d, e, g, f, h, i, user_input;

	while (true) {
		if (y.Banker::curr >= 0.10) {
			y.Banker::curr = y.Banker::curr - 0.10;
			reel_Act1 = (rand() % 7);
			reel_Act2 = (rand() % 7);
			reel_Act3 = (rand() % 7);

			cout << endl;

			top_Row1 = reel_Act1 - 1;
			top_Row2 = reel_Act2 - 1;
			top_Row3 = reel_Act3 - 1;
			top_Row1_ = vector_Correct(top_Row1);
			top_Row2_ = vector_Correct(top_Row2);
			top_Row3_ = vector_Correct(top_Row3);

			bot_Row1 = reel_Act1 + 1;
			bot_Row2 = reel_Act2 + 1;
			bot_Row3 = reel_Act3 + 1;
			bot_Row1_ = vector_Correct(bot_Row1);
			bot_Row2_ = vector_Correct(bot_Row2);
			bot_Row3_ = vector_Correct(bot_Row3);

			a = reel_1[top_Row1_];
			b = reel_2[top_Row2_];
			c = reel_3[top_Row3_];
			d = reel_1[reel_Act1];
			e = reel_2[reel_Act2];
			f = reel_3[reel_Act3];
			g = reel_1[bot_Row1_];
			h = reel_2[bot_Row2_];
			i = reel_3[bot_Row3_];

			system("cls");
			cout << "======================================================================" << endl;
			cout << "=								     =" << endl;
			cout << "=                                   JackPot:  " << std::fixed << std::setprecision(2) << y.Banker::jPot << "		     =" << endl;
			cout << "=                                             ------------	     =" << endl;
			cout << "=      10p Per Play!!!		      Money:  " << std::fixed << std::setprecision(2) << y.Banker::curr << "      	     =" << endl;
			cout << "=                                             ------------	     =" << endl;
			cout << "=								     =" << endl;
			cout << "=               Press 3 To Spin The Reel!!!			     =" << endl;
			cout << "=								     =" << endl;
			cout << "=          " << a << "		" << b << "		" << c << "               =" << endl;
			cout << "=	---" << d << "		" << e << "		" << f << "--- 	     =" << endl;
			cout << "=          " << g << "		" << h << "		" << i << "               =" << endl;
			cout << "=								     =" << endl;
			cout << "======================================================================" << endl;
			cout << endl;
			calcWin(d, e, f);
			help();
		}
		else {
			cout << endl;
			help();
			cin.get();
		}
	}
}

void Machine::calcWin(string d, string e, string f) {
	if (d == "Orange" && e == "Orange" && f == "Orange") {
		y.Banker::curr = y.Banker::curr + 0.50;
		y.Banker::jPot = y.Banker::jPot + 0.10;
		cout << "You Win!!!!" << endl;
		cout << "50p has been added to your Money" << endl;
	};
	if (d == "Melon " && e == "Melon " && f == "Melon ") {
		y.Banker::curr = y.Banker::curr + 1.50;
		y.Banker::jPot = y.Banker::jPot + 0.10;
		cout << "You Win!!!!" << endl;
		cout << "1.50 has been added to your total money" << endl;
	}
	if (d == "  7  " && e == "   7  " && f == "   7  ") {
		y.Banker::curr = y.Banker::curr + y.Banker::jPot;
		cout << "JACKPOT!!!!!!!!!!!!!" << endl;
		cout << "Your Total Is: " << y.Banker::curr << endl;;
		y.Banker::jPot = 0;
	}
}

void Machine::help(){
	cout << "Please Input a number based on what you want to do: " << endl << "1: Input Money " << endl << "2: Output Money" << endl << "3: Continue Playing" << endl;			
	cin >> user_input;
	cout << endl;
	if (user_input == "1") {
		y.Banker::curr = y.Banker::input_Money(y.Banker::curr);
		cout << endl;
	}
	else if (user_input == "2") {
		y.Banker::curr = y.Banker::output_Money(y.Banker::curr);
		cout << endl;
	}
	else {
		y.Banker::jPot = y.Banker::jPot + 0.10;
		cin.get();
	}
}
		

	int Machine::vector_Correct(int p) {
	if (p > 6) {
		return 0;
		}
	else if (p < 0) {
		return 6;
		}
	else if (p >= 0 && p <= 6) {
		return p;
		}
	}
	
