import com.sun.org.apache.bcel.internal.generic.GOTO

fun main() {
    val (a, b) = readln().split(" ").map { it.toInt() }
    var arr = ArrayDeque<Int>()

    for (i in 1 .. a) {
        arr.add(i)
    }


    var arr1 = ArrayDeque<Int>()
    var pos = b - 1
    for (i in 0 until a){
        arr1.add(arr[pos])
        arr[pos] = 0
        var sum = 0
        while (sum < b) {
            pos++
            if (pos >= a) pos -= a
            if (arr[pos] != 0) sum++
            if (i == a - 1) break
        }
        if (pos >= a) pos -= a
    }
    print("<")
    for (i in 0 until a - 1) {
        print("${arr1[i]}, ")
    }
    print("${arr1[a - 1]}")
    print(">")

}