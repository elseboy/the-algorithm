#include <iostream>
using namespace std;

class Log {
public:
  const int LogLevelError;
  const int LogLevelWarning;
  const int LogLevelInfo;

  Log() : LogLevelError(0), LogLevelWarning(1), LogLevelInfo(2) {}

private:
  int m_LogLevel;

public:
  void SetLevel(int level) { m_LogLevel = level; }

  void Error(const char *message) {
    if (m_LogLevel >= LogLevelError)
      cout << "[Error]: " << message << endl;
  }

  void Warn(const char *message) {
    if (m_LogLevel >= LogLevelWarning)
      cout << "[WARNING]: " << message << endl;
  }

  void Info(const char *message) {
    if (m_LogLevel >= LogLevelInfo)
      cout << "[INFO]: " << message << endl;
  }
};

int main() {
  Log log;
  log.SetLevel(log.LogLevelError);
  log.Warn("Hello Log");
  log.Info("Hello Log");
  log.Error("Hello Log");
  return 0;
}
