#include <iostream>
#include <vector>
using namespace std;
#define LOG(x) cout << x << endl

void boolExample() {
  int x = 5;
  bool comparisonResult = x == 5;
  if (comparisonResult) {
    cout << comparisonResult << endl;
  }
}

void loopExample() {
  for (int i = 0; i < 5; i++) {
    cout << "for loop i " << i << endl;
  }

  int i = 0;
  for (;;) {
    cout << ";; loop i " << i++ << endl;
    if (i == 5) {
      break;
    }
  }
}

void pointerExample() {
  int var = 8;
  int *ptr = &var;
  *ptr = 10;
  LOG("after change ptr*, var will also change");
  LOG(var);
  // allocate memory
  char *buffer = new char[8];
  // 's' pointer/array, 'ch' default val, 'n' byte length
  memset(buffer, '0', 8);
  for (int i = 0; i < 8; i++) {
    cout << buffer[i] << " ";
  }
}

int pointerAndReference() {
  // *前面必须跟着type (如int *r) 才是声明指针变量的意思
  // &前面必须跟着type (如int &r) 才是声明参考变量的意思
  // https://www.dazhuanlan.com/chengying/topics/1870482
  int a = 5;
  int &r = a;
  int *p;
  p = &a;
  *p = 10;
  int &r2 = *p;
  r2 = 20;
  cout << a << endl;
  return 0;
}

class Player {
public:
  int x, y;
  int speed;

  Player() : x(0), y(0), speed(0) {}

  void Move(int xa, int ya) {
    x += xa * 3;
    y += ya * 3;
  }

  friend ostream &operator<<(ostream &os, const Player &player) {
    os << "Player: (" << player.x << "," << player.y << ")";
    return os;
  }
};

class Entity {
public:
  float X, Y;
  Entity() {}
  Entity(float x, float y) {
    X = x;
    Y = y;
  }
  void PrintEntity() { cout << X << ", " << Y << endl; }
};

class Object : public Entity {
public:
  const char *Name;
  Object() : Entity(), Name("Default") {}
  Object(float x, float y, const char *name) : Entity(x, y), Name(name) {}
  void PrintObject() { cout << Name << endl; }
};

class NameClass {
  string m_Name;
  mutable int m_DebugCount;

public:
  NameClass() : m_Name(), m_DebugCount(0) {}
  // getter
  const string &GetName() const {
    m_DebugCount++;
    return m_Name;
  }
  // setter
  void SetName(const string &name) { m_Name = name; }
};

class Example {
public:
  Example() { cout << "Created Entity!" << endl; }

  Example(int x) { cout << "Created Entity with " << x << endl; }
};

class InitListsClass {
  string m_Name;
  Example m_Example;

public:
  InitListsClass() : m_Example(Example(8)) { m_Name = string("Unknown"); }
  /**
  // 如果以上面的构造器方式构造
  // 它会创建2个Example object,
  // 一个为空参object，另外一个x=8的object
  */
  // InitListsClass() {
  //  m_Name = string("Unknown");
  //  m_Example = Example(8);
  // }
  InitListsClass(const string &name) : m_Name(name) {}
  const string &GetName() const { return m_Name; }
};

class StackAndHeap {
  string m_Name;

public:
  StackAndHeap() : m_Name("Default"){};
  StackAndHeap(const string &name) : m_Name(name) {}
  const string &GetName() const { return m_Name; }
};

class String {

  char *m_Buffer;
  unsigned int m_Size;

public:
  String(const char *string) {
    m_Size = strlen(string);
    m_Buffer = new char[m_Size + 1];
    memcpy(m_Buffer, string, m_Size);
    m_Buffer[m_Size] = 0;
  }

  String(const String &other) : m_Size(other.m_Size) {
    m_Buffer = new char[m_Size + 1];
    memcpy(m_Buffer, other.m_Buffer, m_Size + 1);
  }

  ~String() { delete[] m_Buffer; }

  char &operator[](unsigned int index) { return m_Buffer[index]; }

  friend std::ostream &operator<<(std::ostream &stream, const String &string);
};

std::ostream &operator<<(std::ostream &stream, const String &string) {
  stream << string.m_Buffer;
  return stream;
}

class Arrow {
  int x;

public:
  void Print() const { std::cout << "Hello from Arrow!" << endl; }
};
class ScopePtr {
  Arrow *m_Obj;

public:
  ScopePtr(Arrow *arrow) : m_Obj(arrow) {}

  ~ScopePtr() { delete m_Obj; }

  Arrow *operator->() { return m_Obj; }

  const Arrow *operator->() const { return m_Obj; }
};

struct Vertex {
  float x, y, z;

  Vertex(float x, float y, float z) : x(x), y(y), z(z) {}

  Vertex(const Vertex &vertex) : x(vertex.x), y(vertex.y), z(vertex.z) {
    std::cout << "Copied!" << std::endl;
  }
};

// std::ostream &operator<<(std::ostream &stream, const Vertex &vertex) {
// stream << vertex.x << ", " << vertex.y << ", " << vertex.z;
// return stream;
//}

void FunctionPtr() {
  std::cout << "This is from function pointer!" << std::endl;
}

void PrintValue(int value) { std::cout << "Value: " << value << std::endl; }

void ForEach(const std::vector<int> &values, void (*func)(int)) {
  for (int value : values)
    func(value);
}

int main() {
  cout << "I HATE C++" << endl;
  // boolExample();
  // loopExample();
  // pointerExample();
  // pointerAndReference();
  // ===============
  // Player player;
  // player.Move(2, -2);
  // cout << player << endl;
  // ===============
  // Entity e;
  // e.X = 5;
  // e.Y = 6;
  // e.PrintEntity();
  // Object object(5, 6, "Joma");
  // object.PrintEntity();
  // object.PrintObject();
  // ===============
  // NameClass n;
  // n.SetName("Joma");
  // cout << n.GetName() << endl;
  // InitListsClass c0;
  // ---------------
  // Stack Object
  /*StackAndHeap StackEntity(
      "Recommend way to init object since it is manageable!");
  std::cout << StackEntity.GetName() << std::endl;*/

  // Heap Object
  /*StackAndHeap *HeapEntity =
      new StackAndHeap("Try aviod to create heap object!");
  std::cout << HeapEntity->GetName() << std::endl;
  delete HeapEntity;*/
  // ==============
  // String string = "Joma";
  // String second = string;
  // second[2] = 'a';
  // std::cout << string << std ::endl;
  // std::cout << second << std ::endl;
  const ScopePtr entity = new Arrow();
  entity->Print();

  std::vector<Vertex> vertices;
  vertices.reserve(3);
  vertices.emplace_back(1, 2, 3);
  vertices.emplace_back(4, 5, 6);
  vertices.emplace_back(7, 8, 9);

  // for (int i = 0; i < vertices.size(); i++) {
  // std::cout << "Vertex " << i << ": " << vertices[i] << std::endl;
  //}

  // for (Vertex &v : vertices)
  // std::cout << v << std::endl;

  auto function = FunctionPtr; // equals &FunctionPtr
  std::vector<int> values = {1, 2, 3, 4, 5};
  ForEach(values, PrintValue);
  return 0;
}
