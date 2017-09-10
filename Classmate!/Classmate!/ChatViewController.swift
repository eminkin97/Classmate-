//
//  ChatViewController.swift
//  Classmate
//
//  Created by Darshan Kalola on 9/9/17.
//  Copyright © 2017 Darshan Kalola. All rights reserved.
//

import UIKit

class ChatViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {
    
    // MARK: - Model
    var currentClass: Class?

    // MARK: - String constants
    let individualMessageIndentifier = "Individual Message"
    
    // MARK: - Outlets
    @IBOutlet var tableView: UITableView!
    @IBOutlet var messageTextField: UITextField!
    
    // MARK: - Table view delegate methods
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: individualMessageIndentifier)
        
        let messageArray = Array(currentClass!.sentMessages!.keys)
        
        cell?.textLabel?.text = messageArray[indexPath.row]
        return cell!
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return (currentClass?.sentMessages?.count)!
    }
}
