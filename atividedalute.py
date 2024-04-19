void main() {
    salute (name: 'Adrian', age: 19);
}

void salute({
required String name,
String? sep,
int? age
}) {
    print('Saudação do ${name}');
    if(sep != null) {
        print(sep * 25);
    }
    if(age != null) {
        print(age);
    }
    print(DateTime.now());
}
