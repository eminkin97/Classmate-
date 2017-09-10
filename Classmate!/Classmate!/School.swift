//
//  School.swift
//  Classmate
//
//  Created by Darshan Kalola on 9/8/17.
//  Copyright © 2017 Darshan Kalola. All rights reserved.
//

import Foundation
import UIKit

class School {
    // A dictionary with key of subject with relevant class codes
    var subjectsWithClassCodes: [String : [String]]?
    
    init(loadSubjects: [String : [String]]) {
        subjectsWithClassCodes = loadSubjects
    }
    
    // Gets all available subjects in the school
    func getAllSubjects() -> [String] {
        let subjects = Array(subjectsWithClassCodes!.keys)
        return subjects
    }
    
    // Gets class codes from a given subject
    func getAllClassCodesFromSubject(withSubject subject: String) -> [String] {
        return subjectsWithClassCodes![subject]!
    }
}
