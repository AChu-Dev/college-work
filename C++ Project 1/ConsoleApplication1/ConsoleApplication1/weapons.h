#pragma once
# include <string>

class Robot {
protected:
	void set_name(std::string s);
	void change_name();
	std::string get_name();
	void introduce_self();
	std::string name = "Unnamed Weapon";
};

class Cleaning: protected Robot {
public:
	void clean_rooms();
};

class Cooking : protected Robot {
public:
	void gril_steak();
	void prepare_food(str::string a);
	void prepare_food(str::string a, str::string b);
};