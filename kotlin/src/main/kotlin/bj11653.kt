fun main() {
    var inp = 0
    while (true) {
        inp = readln().toInt()
        if (inp == -1) return
        var sum = 0
        var arr: MutableList<Int> = arrayListOf()

        for (i in 1 .. inp / 2) {
            if (inp % i == 0) {
                sum += i
                arr.add(i)
            }
        }
        if (sum == inp) {
            print("$inp = ")
            for (i in 0 until arr.size - 1) {
                print("${arr[i]} + ")
            }
            println("${arr[arr.size - 1]}")
        } else {
            println("$inp is NOT perfect.")
        }
    }
}