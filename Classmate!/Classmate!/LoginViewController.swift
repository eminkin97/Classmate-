//
//  LoginViewController.swift
//  Classmate
//
//  Created by Darshan Kalola on 9/9/17.
//  Copyright © 2017 Darshan Kalola. All rights reserved.
//

import UIKit

class LoginViewController: UIViewController {
    
    // MARK: - String contants
    let loginButtonSegue = "Login"
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        
        // Set up button
        loginButton.layer.cornerRadius = 15
        loginButton.layer.masksToBounds = true
    }
    
    @IBOutlet var loginButton: UIButton!
    
    // Returns to sign in screen
    @IBAction func cancel(_ sender: UIBarButtonItem) {
        dismiss(animated: true, completion: nil)
    }
}
