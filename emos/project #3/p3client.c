#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <dirent.h>
#include <ctype.h>
#include <pthread.h> //pthread 헤더
#define SERV_IP "220.149.128.103" 
#define SERV_PORT 4538
#define CLIT_IP "220.149.128.102" //클라이언트 IP
#define CLIT_PORT "4537" //클라이언트 포트 번호
#define CLIT_PORT_INT 4537
pthread_t chatview;//채팅을 출력 위해 만든 쓰레드
pthread_t chatwrite;//채팅을 입력해 서버로 전송하기 위해 만든 쓰레드
pthread_t sendfile;//파일을 보내기 위해 만든 쓰레드
pthread_t recvfile;//파일을 받기 위해 만든 쓰레드
char sendmessage[100]; //3번 문제에서 서버에서 받은 포트와 IP의 정보값
struct flag { //플래그를 구조체로 생성하였다.
	int sockfd; //소켓
	int rcv_byte; 
	int writeFlag; //클라이언트 화면에 출력하는 플래그 
	int exitFlag; //클라이언트 종료 플래그
};
struct flag c;
int recv_t(int socket, char* buf, int buff, int i) {//흐름 보기 위해 만든 함수
	int t;
	t = recv(socket, buf, buff, 0);
	return t;
}
int send_t(int socket, char* buf, int buff, int i) {//흐름 보기 위해 만든 함수
	int t;
	t = send(socket, buf, buff, 0);
	if (t > -1) {
		//printf("send : %d, %d\n", i,t);
	}
	return t;
}

void cleanup(void* argu) {
	int socket = *((int*)argu);
	printf("clean");
	close(socket); //서버 역할을 하는 클라이언트의 소켓을 닫음 
	printf("----------END SEND----------\n");
}

void* recvfile_thread(void* argu) { 
	//쓰레드 recvfile가 수행할 함수, 메시지를 받아 파일에 복사하는 기능을 한다.
	int recv_sockfd, recv_new_fd;
	struct sockaddr_in my_addr;
	struct sockaddr_in their_addr;
	unsigned int sin_size;
	FILE* pFile = NULL;
	int rcv_byte;
	char buf[512];
	char arg[512];
	char filename[25]; //파일 제목
	char choose[10] = "";
	int val = 1;
	printf("\n----------FILE SEND----------\n");
	FILE* rFile = NULL;
	/*server*/
	recv_sockfd = socket(AF_INET, SOCK_STREAM, 0);
	pthread_setcancelstate(PTHREAD_CANCEL_ENABLE, NULL);
	pthread_cleanup_push(cleanup, (void*)&recv_sockfd);//pthread_cancel 콜백 함수 등록
	pthread_setcanceltype(PTHREAD_CANCEL_ASYNCHRONOUS, NULL);//pthread_cancel시 바로 종료
	if (recv_sockfd == -1) {
		perror("Server-socket() error lol!");
		exit(1);
	}
	else printf("Server-socket() sockfd is OK...\n");
	/* host byte order */
	my_addr.sin_family = AF_INET;
	/* short, network byte order */
	my_addr.sin_port = htons(CLIT_PORT_INT);
	my_addr.sin_addr.s_addr = INADDR_ANY;
	/* zero the rest of the struct */
	memset(&(my_addr.sin_zero), 0, 8);
	/* to prevent ‘Address already in use…’ */
	if (setsockopt(recv_sockfd, SOL_SOCKET, SO_REUSEADDR, (char*)&val, sizeof(val)) < 0)
	{
		perror("setsockopt");
		close(recv_sockfd);
		exit(1);
		//return -1;
	}
	/* bind */
	if (bind(recv_sockfd, (struct sockaddr*) & my_addr, sizeof(struct sockaddr)) == -1)
	{
		perror("Server-bind() error lol!");
		exit(1);
	}
	else printf("Server-bind() is OK...\n");
	/* listen */
	if (listen(recv_sockfd, 10) == -1)
	{
		perror("listen() error lol!");
		exit(1);
	}
	else printf("listen() is OK...\n\n");
	/* ...other codes to read the received data... */
	sin_size = sizeof(struct sockaddr_in);
	recv_new_fd = accept(recv_sockfd, (struct sockaddr*) & their_addr, &sin_size);
	if (recv_new_fd == -1) {
		perror("accept() is error lol!...");
		exit(1);
	}
	else printf("accept() is OK...\n");
	/* receive file msg */
	rcv_byte = recv(recv_new_fd, buf, sizeof(buf), 0); //recvfile i = 1 리스트를 받음 
	printf("%s\n", buf);
	fgets(choose, sizeof(choose), stdin);//리스트를 보고 가져오고싶은 txt파일을 고름
	send_t(recv_new_fd, choose, sizeof(choose), 100);//recvfile i = 2 그 번호를 전송함 
	strcpy(buf, "");
	rcv_byte = recv(recv_new_fd, filename, sizeof(filename), 0);//recvfile i = 3 해당 번호의 제목을 받아옴
	if (rcv_byte > -1) {
		rFile = fopen(filename, "w");
		//번호의 제목으로 파일을 받아옴, 이때 모드는 w로 해당 파일이 존재할때 
		//초기화하고 클라이언트 역할을하는 클라이언트의 받아온 문서로 변경함
		if (rFile == NULL) { //실패시
			printf("failed to makefile\n");
		}
		else {
			send_t(recv_new_fd, "ack", 4, 200);//recvfile i = 4 확인신호 전송
			rcv_byte = recv(recv_new_fd, arg, sizeof(arg), 0);//recvfile i = 5 내용을 받아옴
			if (strcmp(arg, "exit") != 0) {
				fputs(arg, rFile); //파일에 내용을 입력함
			}
		}
	}
	/*close*/
	pthread_cleanup_pop(0);
	fclose(rFile); //파일을 닫음
	close(recv_new_fd); //클라이언트 역할을 하는 클라이언트의 accept값을 닫음
	close(recv_sockfd); //서버 역할을 하는 클라이언트의 소켓을 닫음 
	printf("\n----------END SEND----------\n");
	return 0;
}

void* sendfile_thread(void* argu){
//쓰레드 sendfile가 수행할 함수, 메시지를 받아 파일에 복사하는 기능을 한다.
	char dirindex[20][25]; //현재 파일 개수 최대 20개까지 받을 수 있음
	char filename[25]; // 파일 제목
	char sendmsg[512] = ""; //파일 리스트
	int	i = 0;
	char charchoose[10] = ""; 
	char updatechoose[5] = ""; //charchoose와 updatechoose는 받고자하는 클라이언트가 고른 txt파일의 리스트 번호
	int choose=-1; //char -> int 형으로 변환한 리스트 번호
	DIR* dir; 
	struct dirent* list;
	int Flag = 0;
	/*sendmessage 이용할 수 있는 데이터로 변환하는 과정*/
	char* cut = strtok(sendmessage, "/");    //첫번째 strtok 사용. 
	char* fd = "";
	char* ad = "";
	char* po = "";
	int port = 0; //int형으로 변환한 po
	char addr[14]; //고정 크기로 변환한 ad
	FILE* pFile = NULL;
	int send_sockfd; /* will hold the destination addr */
	struct sockaddr_in dest_addr;
	int rcv_byte;
	char filemsg[512];
	char buf[512];
	while (cut != NULL)              //ptr이 NULL일때까지 (= strtok 함수가 NULL을 반환할때까지)
	{
		printf("%s\n", cut);
		cut = strtok(NULL, "/");     //자른 문자 다음부터 구분자 또 찾기
		if (strcmp(fd, "") == 0) {
			fd = cut; //제일처음의 파일 전송에서 클라이언트 역할을 할 클라이언트의 인덱스 값
		}
		else if (strcmp(ad, "") == 0) {
			ad = cut; //두번째의 파일 전송에서 클라이언트 역할을 할 클라이언트의 IP
		}
		else if (strcmp(po, "") == 0) {
			po = cut;  //파일 전송에서 클라이언트 역할을 할 클라이언트의 포트
		}
	}
	strcpy(addr, ad); //지역변수로 변환
	port = atoi(po); //int형으로 변환
	//printf("%s/%d", addr, port);
	/*client*/
	send_sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if (send_sockfd == -1)
	{
		perror("Client-socket() error lol!");
		exit(1);
	}
	else printf("Client-socket() sockfd is OK...\n");
	dest_addr.sin_family = AF_INET;
	dest_addr.sin_port = htons(port);
	dest_addr.sin_addr.s_addr = inet_addr(addr);
	memset(&(dest_addr.sin_zero), 0, 8);
	/* connect */
	if (connect(send_sockfd, (struct sockaddr*) & dest_addr, sizeof(struct sockaddr)) == -1)
	{
		perror("Client-connect() error lol");
		exit(1);
	}
	else printf("Client-connect() is OK...\n\n");
	/*send file */
	printf("\n----------FILE SEND----------\n");
	dir = opendir(".");              // 현재 디렉토리를 열기
	if (NULL != dir && i < 50)
	{
		int k = 0;
		while (list = readdir(dir))  // 디렉토리 안에 있는 모든 파일과 디렉토리 출력
		{
			if (strstr(list->d_name, ".txt") != NULL) {
				strcpy(dirindex[i], list->d_name);
				sprintf(sendmsg, "%s%d\t%s\n", sendmsg, i, dirindex[i]); //리스트 생성
				i++;
			}
			else {
				//printf("NULL");
			}
		}
	}
	send_t(send_sockfd, sendmsg, sizeof(sendmsg), 1);//sendfile,i = 1 리스트 전송
	rcv_byte = recv(send_sockfd, charchoose, sizeof(charchoose), 0);
	for(int p = 0; p < strlen(charchoose) + 1; p++) {
		if (charchoose[p] == '\n') {
			break;
		}
		else {
			updatechoose[p] = charchoose[p]; //리스트 번호를 옮김
			if (isdigit(updatechoose[p]) == 0) {
				printf("\n----------END SEND----------\n");
				rcv_byte = recv(send_sockfd, buf, sizeof(buf), 0);//sendfile i = 4 확인신호를 받음
				send_t(send_sockfd, "exit", 5, 300);//sendfile i = 5 내용을 전송
				close(send_sockfd); //send socket 닫음
				pthread_exit(NULL); //쓰레드 종료
			}
		}
	}
	choose = atoi(updatechoose); //int로 변환 
	for (int j = 0; j < i; j++) { //i 크기만큼 (i = 현재 디렉토리에서 파일의 갯수) 
		if (j == choose) { //찾으면
			printf("client is choose %s\n", dirindex[j]);
			strcpy(filename, dirindex[j]);
			send_t(send_sockfd, filename, sizeof(filename), 3);//sendfile i=3 제목을 보냄
			break;
		}
		else {
			//printf("no\n"); //없으면 없다고 출력
		}
	}
	pFile = fopen(filename, "r"); //해당 파일을 염
	while (1) {
		char arr[50];
		char* ptr = fgets(arr, 50, pFile);
		if (ptr == NULL) { //해당 줄이 NULL일때까지
			break;
		}
		sprintf(filemsg, "%s%s", filemsg, ptr); //sprintf로 string을 만든다.
	}
	rcv_byte = recv(send_sockfd, buf, sizeof(buf), 0);//sendfile i = 4 확인신호를 받음
	//printf("%s", filemsg);
	send_t(send_sockfd, filemsg, strlen(filemsg)+1, 300);//sendfile i = 5 내용을 전송
	printf("\n----------END SEND----------\n");
	/*end*/
	fclose(pFile); //파일 닫음
	close(send_sockfd); //send socket 닫음
	pthread_exit(NULL); //쓰레드 종료
}
void* chatview_thread(void* argu) { // 쓰레드 chatview가 실행하는 함수
	char recvBuf[512];
	char resultBuf[512];
	char message[512];
	while (1) {
		c.rcv_byte = recv_t(c.sockfd, recvBuf, 512, 12);
		if (c.rcv_byte > -1) { //받으면
			if (c.writeFlag == 0) { //자신이 보낸 채팅이 아니면
				if (strncmp(recvBuf, "SENDFILEUSERQPWOEIRUTY", 22) == 0) { 
					//서버에서 파일 전송의 클라이언트 역할을 하게 되었다는 문구를 받으면
					strcpy(sendmessage, recvBuf); //전역변수로 옮김
					pthread_create(&sendfile, NULL, &sendfile_thread, NULL); //sendfile 쓰레드 생성
					//printf("hi~ : %s", recvBuf);
					pthread_join(sendfile, NULL); //쓰레드 종료시 까지 기다림
				}
				else if (strncmp(recvBuf, "sendmsg", 8) == 0) {
					printf("\n");
				}
				else if (strncmp(recvBuf, "sendmnsogt",11) == 0) {
					pthread_cancel(recvfile);
				}
				else {
					printf("%s", recvBuf); //출력
				}
			}
			else {
				c.writeFlag = 0;
			}
		}
		if (c.exitFlag == 1) { //종료 플래그가 1이면
			//printf("bye");
			pthread_exit(NULL); //쓰레드 종료
		}
	}
	return NULL;
}
void* chatwrite_thread(void* argu) { //쓰레드 chatwrite가 실행하는 함수
	char buf[512];
	int t;
	int index = 0;
	char message[512];
	strcpy(message, "");
	while (1) {
		//printf("message: %s",message);
		fgets(message, sizeof(message), stdin); // 메시지를 입력받음
		c.writeFlag = 1; //입력한 메시지가 있으면 자신이 보냈다는 것을 알기 위해 writeflag를 1로 변경해서 
		t = send_t(c.sockfd, message, sizeof(message), 13); //서버로 전송
		if (strncmp(message, "[FILE", 5) == 0) { //[FILE ~를 치면
			pthread_create(&recvfile, NULL, &recvfile_thread, NULL); //파일 전송 쓰레드로 전송
			pthread_join(recvfile, NULL); //쓰레드 종료시 까지 기다림
			send_t(c.sockfd, "endsend", 8, 15);//recvfile
			continue;
		}
		if (strcmp(message, ":q\n") == 0) { //:q를 치면
			//printf("bye");
			c.exitFlag = 1; //exitFlag 1로 변경후
			strcpy(message, "");
			pthread_exit(NULL); //쓰레드 종료
		}
		//}
	}
	return NULL;
}
int main(int argc, char* argv[]) {
	struct sockaddr_in dest_addr;
	char buf[512];
	char buf2[512];
	char id[20];
	char pw[20];
	char chatReceive[512];
	c.writeFlag = 0;
	c.exitFlag = 0;
	c.sockfd = socket(AF_INET, SOCK_STREAM, 0);
	c.exitFlag = 0;
	if (c.sockfd == -1)
	{
		perror("client-socket() error lol!");
		exit(1);
	}
	else printf("client-socket() sockfd is OK...\n");
	dest_addr.sin_family = AF_INET;
	dest_addr.sin_port = htons(SERV_PORT);
	dest_addr.sin_addr.s_addr = inet_addr(SERV_IP);

	memset(&(dest_addr.sin_zero), 0, 8);

	if (connect(c.sockfd, (struct sockaddr*) & dest_addr, sizeof(struct sockaddr)) == -1) {
		perror("client-connect() error lol");
		exit(1);
	}
	else printf("client-connect() is ok...\n");
	c.rcv_byte = recv_t(c.sockfd, buf, sizeof(buf), 1);// i = 1 서버에서 환영하는 메시지 받음 
	printf("%s\n", buf);
	printf("id: ");
	scanf("%s", id);
	send_t(c.sockfd, id, strlen(id) + 1, 2);//i = 2 id를 전송
	c.rcv_byte = recv_t(c.sockfd, buf, sizeof(buf), 3);//i = 3 확인 받음
	printf("pw: ");
	scanf("%s", pw);
	send_t(c.sockfd, pw, strlen(pw) + 1, 4);//i = 4 pw를 전송
	c.rcv_byte = recv_t(c.sockfd, buf, sizeof(buf), 5);//i = 5 서버에서  로그인 메시지 받음
	printf("buf :%s\n", buf); //로그인 메시지 출력
	send_t(c.sockfd, "ack", 4, 6);//i = 6 로그인 완료 확인 신호를 보냄 
	//port
	strcpy(buf, "");
	printf("buf: %s\n", buf);
	c.rcv_byte = recv_t(c.sockfd, buf, sizeof(buf), 7);//7 로그인 서버에서 확인 신호를 받음
	printf("buf: %s\n", buf);
	if (strcmp(buf, "new") != 0) { //만약 재접속이 아니라면
		send_t(c.sockfd, CLIT_IP, sizeof(CLIT_IP), 8);//분기 1, 8 이 클라이언트의 IP를 보냄
		c.rcv_byte = recv_t(c.sockfd, buf, sizeof(buf), 9);//분기 1, 9확인 신호를 받음 
		send_t(c.sockfd, CLIT_PORT, sizeof(CLIT_PORT), 10);//분기 1, 10 이 클라이언트의 PORt를 받음
	}
	else {
		send_t(c.sockfd, "ack", 4, 8);//분기 2, i = 8
	}
	//chat
	c.rcv_byte = recv_t(c.sockfd, buf2, sizeof(buf2), 11);//분기 1일땐 i = 9, 분기 2일땐 i = 9
	printf("buf: %s\n", buf2);
	if (strcmp(buf2, "chat") == 0 || strcmp(buf2, "new") == 0) { //buf2가 
		printf("---------------Chatting Room---------------\n");
		pthread_create(&chatview, NULL, &chatview_thread, NULL); //채팅 쓰레드 생성
		pthread_create(&chatwrite, NULL, &chatwrite_thread, NULL); 
		pthread_join(chatwrite, NULL);// :q 눌려서 쓰레드 끝날때까지 대기
		pthread_join(chatview, NULL);
	}
	//printf("exit %d", c.exitFlag);
	close(c.sockfd); //:q눌리면 소켓을 닫고
	exit(0); // 프로세스 종료
}

