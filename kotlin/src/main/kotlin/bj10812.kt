fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    var arr = Array (n) { it + 1}.toMutableList()
    for (i in 0 until m) {
        var (start, end, mid) = readln().split(" ").map { it.toInt() }
        start--
        end--
        mid--

        arr = (arr.slice(0 until start) + arr.slice(mid .. end) + arr.slice(start until mid) + arr.slice(end + 1 until n)).toMutableList()
    }

    for (i in arr) {
        print("$i ")
    }
}

//[9, 10, 1, 2, 3, 4, 5, 6, 7, 8]