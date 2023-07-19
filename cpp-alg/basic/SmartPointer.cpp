#include <iostream>
#include <memory>
#include <string>

class Entity {
public:
  Entity() { std::cout << "Created entity Class!" << std::endl; }
  ~Entity() { std::cout << "Destroyed entity Class!" << std::endl; }

  void Print(std::string str) {
    std::cout << "This is from " << str << std::endl;
  }
};

int main() {
  // level 1
  {
    // it will not be destoryed after level 2 {} because there is still
    // referencing to e0, unless after level 1 {} scope
    //
    // but if set std::weak_ptr<Entity> e0, it will be destroyed after level 2
    // {} becasue weak_ptr does not increase the reference count, so there is
    // only 1 reference, after level 1 {}, it will be gone
    std::shared_ptr<Entity> e0;
    // level 2 {}
    {
      // unique_ptr is slightly safer
      // std::unique_ptr<Entity> pointer = std::make_unique<Entity>();
      // pointer->Print("pointer");

      // can not take a copy since it is unique
      // std::unique_ptr<Entity> copy(pointer);

      // std::move will trasfer pointer to copy, pointer will be nullptr
      // std::unique_ptr<Entity> copy = std::move(pointer);
      // copy->Print("copy");

      // shared_ptr uses count to track originly object is still referencing, if
      // turns to 0, it means there is no more referencing, it will remain vaild
      // but points to a deleted object"dangling pointer"
      std::shared_ptr<Entity> shared = std::make_shared<Entity>();
      e0 = shared;
      shared->Print("shared");
    }
  }
}
