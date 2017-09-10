//
//  RegisterViewController.swift
//  Classmate!
//
//  Created by Darshan Kalola on 9/9/17.
//  Copyright © 2017 Darshan Kalola. All rights reserved.
//

import UIKit

class RegisterViewController: UIViewController {

    @IBOutlet var registerButton: UIButton!
    
    let backendURLForAuth = "http://127.0.0.1:8000/auth"
    var schoolName = ""
    
    // MARK: - Model
    var user: User?
    
    @IBOutlet var email: HoshiTextField!
    @IBOutlet var name: HoshiTextField!
    @IBOutlet var password: HoshiTextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Set up button
        registerButton.layer.cornerRadius = 15.0
        registerButton.layer.masksToBounds = true
    }
    
    @IBAction func cancelButton(_ sender: UIBarButtonItem) {
        dismiss(animated: true, completion: nil)
    }
    
    func setUserInformation() {
        let fetchUrl = URL(string: backendURLForAuth)
        
        let emailText = email.text!
        let nameText = name.text!
        let passwordText = password.text!
        
        let postString = "email=\(emailText)&username=\(nameText)&password=\(passwordText)"
        
        var request = URLRequest(url: URL(string: "\(fetchUrl!)?\(postString)")!)
        request.httpMethod = "GET"
        
        let task = URLSession.shared.dataTask(with: request) { (data, response, error) in
            print("THIS IS WORKING!")
            guard let data = data, error == nil else {
                print(error!)
                return
            }
            
            if let httpStatus = response as? HTTPURLResponse, httpStatus.statusCode != 200 {

                // check for http errors
                print("statusCode should be 200, but is \(httpStatus.statusCode)")
                print("response = \(response!)")
            }
            
            let responseString = String(data: data, encoding: .utf8)
            self.schoolName = self.parseStringForSchool(withString: responseString!)
            
            // Set up the model
            self.user?.name = nameText
            self.user?.email = emailText
            self.user?.password = passwordText
        }
        task.resume()
    }
    
    func getClassCodes(withSchoolName schooName: String) {
        let fetchUrl = URL(string: backendURLForAuth)
        let request = URLRequest(url: fetchUrl!)
        
        let task = URLSession.shared.dataTask(with: request) { (data, response, error) in
            guard let finalData = data, error == nil else {
                print(error!)
                return
            }
            
            if let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode != 200 {
                print("Response is an error response with code of \(httpResponse.statusCode)")
            }
            
            let responseString = String(data: finalData, encoding: .utf8)
            print("Class code response \(responseString!)")
            
        }
        task.resume()
    }
    
    @IBAction func register(_ sender: Any) {
        setUserInformation()
        getClassCodes(withSchoolName: schoolName)
        
        performSegue(withIdentifier: "Finish Register", sender: nil)
    }
    
    
    func parseStringForSchool(withString string: String) -> String {
        let range = string.range(of: "\"name\":\"")
        let newStartString = string.substring(from: (range?.upperBound)!)
        var finalString = ""
        
        for singleChar in newStartString.characters {
            if singleChar == "\"" {
                break
            }
            finalString.append(singleChar)
        }
        return finalString
    }
}


