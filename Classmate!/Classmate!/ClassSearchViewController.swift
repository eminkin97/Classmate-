//
//  ClassSearchViewController.swift
//  Classmate
//
//  Created by Darshan Kalola on 9/8/17.
//  Copyright © 2017 Darshan Kalola. All rights reserved.
//

import UIKit

class ClassSearchViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {

    // MARK: - String constants
    let classCodeCellIdentifier = "Class Code"
    
    @IBOutlet var classCodeSelectTableView: UITableView!
    
    // MARK: - Model
    var school: School?
    var classesShownInDisplay: [String]?
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell(style: .default, reuseIdentifier: classCodeCellIdentifier)

        cell.textLabel?.text = "MAT128"
        return cell
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 5
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        classCodeSelectTableView.reloadData()
    }
}
