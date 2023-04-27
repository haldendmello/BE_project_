// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.8.16;

// import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
contract mini {
    uint256 amt;
    uint256 val;
uint256 intrest=2;
    // constructor() public {}

    struct borower {
        uint score;
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
        uint256 no_of_depeden) public returns (string memory) {
        // TODO: add loan wala in function
        address addr = msg.sender;
        if (pos == 0) {
            borower memory b;
            b.name = name;
            b.aadhar = aadhar;
            b.email = email;
            b.pan=pan;
            b.score=score;
            b.phone=phone;
            b.gender=gender;
            b.a_income=a_income;
            b.no_of_dependents=no_of_depeden;
            b.loan_amountt=0;
            b.l_purpose="";
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

    function sendmoney(address payable to,uint256 paisaa) public payable returns (uint256) {
        // amt=amountt
        // amt=amountt;
        // return amountt;
        // 0xab594600376ec9fd91f8e885dadf0ce036862de0 matic/usd
        // require(getConversion(1*1e10) >= 0,"ERROR NO funds"); //1*10**18=100000000000000000 wei / 1 ether (set a min limit of 1 ethr)
        // getConversion(msg.value);
        // getConversion(msg.value)
        aa = paisaa * intrest;
        to.transfer(aa);
        return aa;
    }

    function getBalance() public view returns (uint256, uint256) {
        // var time=now;
        return (aa, block.timestamp);
    }

    function l_l()public view returns(address[] memory){
        return loans;
    }

    function get_borrower(address addr)public view returns (string memory, string memory,string memory,string memory,uint256,uint256,string memory ){
        // if(keccak256(patientInfo[addr].name) == keccak256(""))revert();
        return (borowerInfo[addr].name, borowerInfo[addr].aadhar, borowerInfo[addr].pan, borowerInfo[addr].email,borowerInfo[addr].phone, borowerInfo[addr].score,borowerInfo[addr].loan_amountt,borowerInfo[addr].l_purpose);
    }

    function get_lender(address addr) view public  returns (string memory, string memory,string memory,string memory) {
        // if(keccak256(doctorInfo[addr].name)==keccak256(""))revert();
        return (lenderInfo[addr].name, lenderInfo[addr].email, lenderInfo[addr].pan, lenderInfo[addr].aadhar);
    }

    function get_borrower_list() public view returns (address[] memory) {
        return borower_list;
    }

    function get_lender_list() public view returns (address[] memory) {
        return lender_list;
    }
    function reg_loan(address acc_address,uint l_amount, string memory purpose)public  {
        // string memory a=keccak256(l_amount+purpose);
        borowerInfo[acc_address].loan_amountt=l_amount;
        borowerInfo[acc_address].l_purpose=purpose;
        loans.push(acc_address);
        // loans.push(keccak256(abi.encodePacked(string.concat(l_amount,purpose))));
    // return keccak256(l_amount+purpose);
    }

    // function getprice()public view returns(uint256){
    //     AggregatorV3Interface interfacee = AggregatorV3Interface(0xAB594600376Ec9fD91F8e885dADF0CE036862dE0);
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
