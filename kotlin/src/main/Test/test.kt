package com.example.bindingTutorial

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.bindingTutorial.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.test_button.setOnClickListener {
            // test_button 클릭 시
            }
        }
    }
}