//
//  ClassMessagesTableViewController.swift
//  Classmate
//
//  Created by Darshan Kalola on 9/8/17.
//  Copyright © 2017 Darshan Kalola. All rights reserved.
//

import UIKit

class ClassMessagesTableViewController: UITableViewController {

    // MARK: - String constants
    let chatCellIdentifier = "Class Chat Cell"
    let unwindSegue = "Unwind"
    
    // MARK: - Model
    var user: User?
    
    // MARK: - Outlets
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // return (user?.classes?.count)!
        return 5
    }
    
    @IBAction func logout(_ sender: UIBarButtonItem) {
        performSegue(withIdentifier: unwindSegue, sender: self)
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let cell = tableView.dequeueReusableCell(withIdentifier: chatCellIdentifier)
        
        cell?.textLabel?.text = "Math"
        return cell!
    }
}
