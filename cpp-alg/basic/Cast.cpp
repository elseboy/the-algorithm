#include <iostream>

class Entity {

public:
  virtual void PrintName() {}
};

class Player : public Entity {
public:
};

class Enemy : public Entity {
public:
};

int main() {
  // dynamic cast
  Player *player = new Player();
  Entity *actuallyPlayer = player;

  Entity *actuallyEnemy = new Enemy();

  Player *p0 = dynamic_cast<Player *>(actuallyEnemy);
  Player *p1 = dynamic_cast<Player *>(actuallyPlayer);

  std::cin.get();
  return 0;
}
