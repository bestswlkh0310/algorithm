fun main() {
    val arr = Array (100000) { false }
    for (i in 1 .. 10000) {
        arr[i.toString().toCharArray().sumOf { it - '0' } + i] = true
    }
    for (i in 1.. 10000) {
        if (!arr[i]) {
            println(i)
        }
    }
}