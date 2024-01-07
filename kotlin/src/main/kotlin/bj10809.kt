fun main() {
    var arr = Array (26) { -1 }
    val str = readln().toCharArray()
    for (i in 0 until str.size) {
        if (arr[str[i].code - 97] == -1)
            arr[str[i].code - 97] = i
    }
    for (i in arr) {
        print("$i ")
    }
}