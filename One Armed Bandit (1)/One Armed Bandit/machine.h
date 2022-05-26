#include <string>
#include <vector>
#include "banker.h"


class Machine{
public:
	Banker y;
	Machine();
	void attract_Mode();
	void spin_Reels();
	void help();
protected:
	std::vector<std::string> reel_1;
	std::vector<std::string> reel_2;
	std::vector<std::string> reel_3;
	int vector_Correct(int a);
	void calcWin(std::string d, std::string e, std::string f);

	int reel_Act1, reel_Act2, reel_Act3, top_Row1, top_Row2, top_Row3, top_Row1_, top_Row2_, top_Row3_;
	int	bot_Row1, bot_Row2, bot_Row3, bot_Row1_, bot_Row2_, bot_Row3_;
	std::string a, b, c, d, e, g, f, h, i, user_input;

};


