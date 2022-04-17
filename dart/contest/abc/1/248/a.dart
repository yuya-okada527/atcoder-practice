import 'dart:io';

void main() {
  String val = stdin.readLineSync() ?? "";
  for (var i in List<int>.generate(10, (index) => index)) {
    if (!val.contains(i.toString())) {
      print(i);
    }
  }
}
