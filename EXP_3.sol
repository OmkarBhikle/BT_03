// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PalindromeChecker {
    
    function isPalindrome(string memory s) public pure returns (bool) {
        bytes memory strBytes = bytes(s);
        uint256 len = strBytes.length;
        
        for (uint256 i = 0; i < len / 2; i++) {
            if (strBytes[i] != strBytes[len - i - 1]) {
                return false;
            }
        }
        
        return true;
    }
}
