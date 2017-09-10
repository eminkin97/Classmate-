//
//  SignInViewController.swift
//  Classmate!
//
//  Created by Darshan Kalola on 9/9/17.
//  Copyright © 2017 Darshan Kalola. All rights reserved.
//

import UIKit

class SignInViewController: UIViewController {

    // MARK: - String constants
    let loginSegue = "Login Segue"
    let registerSegue = "Register Segue"
    
    @IBAction func loginTapped(_ sender: UITapGestureRecognizer) {
        performSegue(withIdentifier: loginSegue, sender: nil)
    }
    
    @IBAction func registerTapped(_ sender: UITapGestureRecognizer) {
        performSegue(withIdentifier: registerSegue, sender: nil)
    }

    // MARK: - Lifecycle methods
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        
        self.navigationController?.setNavigationBarHidden(true, animated: true)
    }
    
    // Unwind segue
    @IBAction func prepareForUnwind(segue: UIStoryboardSegue) {
    
    }
    
}
