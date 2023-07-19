#include <chrono>
#include <iostream>
#include <thread>

static bool s_Finished = false;

void Work() {

  using namespace std::literals::chrono_literals;
  while (!s_Finished) {
    std::cout << "Working...\n";
    std::this_thread::sleep_for(1s);
  }
}

struct Timer {
  std::chrono::time_point<std::chrono::steady_clock> start, end;
  std::chrono::duration<float> duration;

  Timer() { start = std::chrono::high_resolution_clock::now(); }

  ~Timer() {
    end = std::chrono::high_resolution_clock::now();
    duration = end - start;
    std::cout << "Time took " << duration.count() << "s" << std::endl;
  }
};

void Task() {
  Timer timer;

  for (int i = 0; i < 100; i++)
    std::cout << "From task!" << std::endl;
}

int main() {

  // std::thread worker(Work);
  // std::cin.get();
  // s_Finished = true;
  // worker.join();
  // std::cout << "Finished!" << std::endl;
  // std::cin.get();

  Task();
  std::cin.get();
}
