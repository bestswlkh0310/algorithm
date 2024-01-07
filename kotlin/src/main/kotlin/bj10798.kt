import java.lang.Exception

fun main() {
    var arr: MutableList<MutableList<Char>> = arrayListOf()
    var size: MutableList<Int> = arrayListOf()
    for (i in 0 until 5) {
        arr.add(readln().toMutableList())
        size.add(arr[i].size)
    }

    for (y in 0 until size.max()) {
        for (x in 0 until 5) {
            try {
                print("${arr[x][y]}")
            } catch (e: Exception) {}
        }
    }
}