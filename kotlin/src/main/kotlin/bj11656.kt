fun main() {
    val str = readln()
    val arr = arrayListOf<String>()
    for (i in 0 until str.length) {
        arr.add(str.slice(i until str.length))
    }
    for (i in arr.sorted()) {
        println(i)
    }
}