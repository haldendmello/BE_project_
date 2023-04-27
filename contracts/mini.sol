// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

// contract mini {
//   constructor() public {
//   }
// }


// pragma solidity >=0.8.16;

// import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
contract mini {
    uint256 amt;
    uint256 val;
    uint256 intrest = 2;
    // constructor() public {}

    struct borower {
        uint256 score;
        string name;
        string email;
        address[] borrower_list;
        string aadhar;
        string pan;
        uint256 phone;
        string gender;
        uint256 a_income;
        uint256 no_of_dependents;
        uint256 loan_amountt;
        string l_purpose;
    }

    struct lender {
        string name;
        string aadhar;
        address[] lender_list;
        string pan;
        string email;
    }
    address[] loans;
    address[] public borower_list;
    address[] public lender_list;

    mapping(address => borower) borowerInfo;
    mapping(address => lender) lenderInfo;
    // var date=new Date();
    // uint deposit;
    // constructor() public {
    //     amt=0;
    //     val=1000;
    // }
    // mapping(address => uint) borower_addr,lender_addr;
    // TODO:ABI bytecode in js
    uint256 PAISA = 10 * 1e10;
    uint256 aa = 1;

    // function user(string memory name,string memory email,uint256 pos,string memory aadhar,string memory pan,uint256 score,uint256 a_income,uint256 no_depends,string memory gender,uint256 phone_no) public returns (string memory) {
    function user(
        string memory name,
        string memory email,
        uint256 pos,
        string memory aadhar,
        string memory pan,
        uint256 score,
        uint256 phone,
        string memory gender,
        uint256 a_income,
        uint256 no_of_depeden
    ) public returns (string memory) {
        // TODO: add loan wala in function
        address addr = msg.sender;
        if (pos == 0) {
            borower memory b;
            b.name = name;
            b.aadhar = aadhar;
            b.email = email;
            b.pan = pan;
            b.score = score;
            b.phone = phone;
            b.gender = gender;
            b.a_income = a_income;
            b.no_of_dependents = no_of_depeden;
            b.loan_amountt = 0;
            b.l_purpose = "";
            borowerInfo[msg.sender] = b;
            borower_list.push(addr);
            return name;
        } else if (pos == 1) {
            lenderInfo[addr].name = name;
            lenderInfo[addr].aadhar = aadhar;
            lenderInfo[addr].pan = pan;
            lenderInfo[addr].email = email;

            lender_list.push(addr);
            return name;
        } else {
            revert();
        }
    }

    function sendmoney(address payable to, uint256 paisaa)
        public
        payable
        returns (uint256)
    {
        // 0xEbaCb721c58F7570c67E2eD4BdFd2367e48734CF-
        // amt=amountt
        // amt=amountt;
        // return amountt;
        // 0xa1079d642a30adf6b7128e592406dc6434366910 matic/usd
        // require(getConversion(1*1e10) >= 0,"ERROR NO funds"); //1*10**18=100000000000000000 wei / 1 ether (set a min limit of 1 ethr)
        // getConversion(msg.value);
        // getConversion(msg.value)
        require(msg.value == paisaa * 100000);
        to.transfer(msg.value);
        return aa;
    }
    function sendmoneyy(address payable to)
        public
        payable
        returns (uint256)
    {
        // amt=amountt
        // amt=amountt;
        // return amountt;
        // 0xa1079d642a30adf6b7128e592406dc6434366910 matic/usd
        // require(getConversion(1*1e10) >= 0,"ERROR NO funds"); //1*10**18=100000000000000000 wei / 1 ether (set a min limit of 1 ethr)
        // getConversion(msg.value);
        // getConversion(msg.value)
        // aa = paisaa * 100000;
        to.transfer(msg.value);
        return msg.value;
    }



    function getBalance() public view returns (uint256, uint256) {
        // var time=now;
        return (aa, block.timestamp);
    }

    function l_l() public view returns (address[] memory) {
        return loans;
    }

    //         uint score;
    //         string name;
    //         string email;
    //         address[] borrower_list;
    //         string aadhar;
    //         string pan;
    //         uint256 phone;
    //         string gender;
    //         uint256 a_income;
    //         uint256 no_of_dependents;
    //         uint256 loan_amountt;
    //         string l_purpose;
    function get_borrower(address addr)
        public
        view
        returns (
            string memory,
            string memory,
            string memory,
            string memory,
            uint256,
            uint256,
            string memory,
            uint256,
            uint256,uint256
        )
    {
        // if(keccak256(patientInfo[addr].name) == keccak256(""))revert();
        borower memory bb = borowerInfo[addr];
        return (
            bb.name,
            bb.aadhar,
            bb.pan,
            bb.email,
           bb.score,
            bb.loan_amountt,
            bb.l_purpose,
           bb.a_income,
           bb.no_of_dependents,
           bb.phone
        );
    }

    function loan_data(address addr)
        public
        view
        returns (
            string memory,
            uint256,
            string memory,
            uint256
        )
    {
        // if(keccak256(patientInfo[addr].name) == keccak256(""))revert();
        return (
            borowerInfo[addr].name,
            borowerInfo[addr].phone,
            borowerInfo[addr].l_purpose,
            borowerInfo[addr].loan_amountt
        );
    }

    function get_lender(address addr)
        public
        view
        returns (
            string memory,
            string memory,
            string memory,
            string memory
        )
    {
        // if(keccak256(doctorInfo[addr].name)==keccak256(""))revert();
        return (
            lenderInfo[addr].name,
            lenderInfo[addr].email,
            lenderInfo[addr].pan,
            lenderInfo[addr].aadhar
        );
    }

    function get_borrower_list() public view returns (address[] memory) {
        return borower_list;
    }

    function get_lender_list() public view returns (address[] memory) {
        return lender_list;
    }

    function reg_loan(
        address acc_address,
        uint256 l_amount,
        string memory purpose
    ) public {
        // string memory a=keccak256(l_amount+purpose);
        borowerInfo[acc_address].loan_amountt = l_amount;
        borowerInfo[acc_address].l_purpose = purpose;
        loans.push(acc_address);
        // loans.push(keccak256(abi.encodePacked(string.concat(l_amount,purpose))));
        // return keccak256(l_amount+purpose);
    }

    // function getprice()public view returns(uint256){
    //     AggregatorV3Interface interfacee = AggregatorV3Interface(0xABc7e638362feaEA6De0299A7eB05AD653A97553);
    //     (,int256 price,,,) = interfacee.latestRoundData();
    //     return uint256(price*1e10);

    // }

    // function getConversion(uint256 amount)public view returns(uint256){
    //     uint256 price=getprice();
    //     uint256 convert_price=(price*amount)/1e18;
    //     return convert_price;

    // }

    // function withdraw(){}

    // function getBalance()public view returns(uint){
    //     return val;
    // }
    // // function getAmt() public view returns(uint){
    //     return amt;
    // }
    // function send() public returns(uint deposit){
    //     val=val-deposit;
    //     amt=val+deposit;
    // }
}
