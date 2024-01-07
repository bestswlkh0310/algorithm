fun main() {
    while (true) {
        var str = readln().toCharArray()
        if (str.joinToString("") == ".") break
        str = str.filter { it == '(' || it == ')' || it == '[' || it == ']' }.toCharArray()
        var str2 = str.joinToString("")
        repeat (str.size) { str2 = str2.replace("[]", "").replace("()", "") }
        if (str2.isEmpty()) println("yes")
        else println("no")
    }
}