import 'dart:io';

void main() {
  // f1();
  f2();
}


void f1() {
  String val = stdin.readLineSync() ?? "";
  for (var i in List<int>.generate(10, (index) => index)) {
    if (!val.contains(i.toString())) {
      print(i);
    }
  }
}

void f2() {
  String? inputStr = stdin.readLineSync();
  if (inputStr == null) return;
  Set<int> input = inputStr.split("").map((i) => int.parse(i)).toSet();
  Set<int> numbers = Set.from(List<int>.generate(10, (index) => index));
  int? ans = numbers.difference(input).first;
  print(ans);
}
