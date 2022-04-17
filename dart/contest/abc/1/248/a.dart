import 'dart:io';

void main() {
  f1();
}


void f1() {
  String val = stdin.readLineSync() ?? "";
  for (var i in List<int>.generate(10, (index) => index)) {
    if (!val.contains(i.toString())) {
      print(i);
    }
  }
}
