// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CertificateRegistry {
    struct Certificate {
        address owner;
        string publicKey;
        bool isRevoked;
        uint256 issueDate;
        uint256 expiryDate;
        string signature;
    }

    mapping(string => Certificate) public certificates;

    function issueCertificate(string memory certID, string memory publicKey, uint256 expiryDate, string memory signature) public {
        require(certificates[certID].owner == address(0), "Certificate already exists");
        certificates[certID] = Certificate(msg.sender, publicKey, false, block.timestamp, expiryDate, signature);
    }

    function revokeCertificate(string memory certID) public {
        require(certificates[certID].owner == msg.sender, "Only owner can revoke");
        certificates[certID].isRevoked = true;
    }

    function verifyCertificate(string memory certID) public view returns (string memory, bool, uint256, uint256, string memory) {
        Certificate memory cert = certificates[certID];
        if (cert.owner == address(0)) return ("", false, 0, 0, "");
        bool valid = !cert.isRevoked && block.timestamp < cert.expiryDate;
        return (cert.publicKey, valid, cert.issueDate, cert.expiryDate, cert.signature);
    }
}
