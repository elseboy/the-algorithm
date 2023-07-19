#include <iostream>
#include <string>

/**
 * An old way to do:
 */
class Singleton {

public:
  static Singleton &Get() { return s_Instance; }

  void Function() {}

private:
  Singleton() {}

  float m_Member = 0.0f;

  static Singleton s_Instance;
};

Singleton Singleton::s_Instance;

int main() {

  Singleton instance = Singleton::Get();

  // Singleton::Get().Function();
  instance.Get();
  return 0;
}
