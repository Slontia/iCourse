package seleniumDemo.Desktop;
//测试注册失败的情况
import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;
import org.junit.*;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.security.Credentials;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;

public class TestRegister {
  WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @Before
  public void setUp() throws Exception {
	  System.setProperty("webdriver.gecko.driver", "C:\\Users\\15061188\\Downloads\\geckodriver-v0.19.0-win32\\geckodriver.exe");
	  driver = new FirefoxDriver();
	  baseUrl = "http://127.0.0.1:8000/";
	  driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
  }

  @Test
  public void testRegister() throws Exception {
    driver.get(baseUrl);
    driver.findElement(By.cssSelector("button.el-button.el-button--text")).click();
    driver.findElement(By.xpath("//body/ul/li[2]")).click();
    driver.findElement(By.cssSelector("input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("input.el-input__inner")).sendKeys("fkd");
    driver.findElement(By.cssSelector("#register_form2 > div.el-form-item__content > div.el-input > input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("#register_form2 > div.el-form-item__content > div.el-input > input.el-input__inner")).sendKeys("方科栋");
    driver.findElement(By.cssSelector("div.el-select > div.el-input > input.el-input__inner")).click();
    driver.findElement(By.cssSelector("li.el-select-dropdown__item")).click();
    driver.findElement(By.cssSelector("#register_form4 > div.el-form-item__content > div.el-input > input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("#register_form4 > div.el-form-item__content > div.el-input > input.el-input__inner")).sendKeys("123456");
    driver.findElement(By.cssSelector("#register_form5 > div.el-form-item__content > div.el-input > input.el-input__inner")).click();
    driver.findElement(By.cssSelector("#register_form5 > div.el-form-item__content > div.el-input > input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("#register_form5 > div.el-form-item__content > div.el-input > input.el-input__inner")).sendKeys("123456");
    driver.findElement(By.cssSelector("#register_form6 > div.el-form-item__content > div.el-input > input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("#register_form6 > div.el-form-item__content > div.el-input > input.el-input__inner")).sendKeys("fang");
    driver.findElement(By.cssSelector("#register_form6 > div.el-form-item__content > div.el-input > input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("#register_form6 > div.el-form-item__content > div.el-input > input.el-input__inner")).sendKeys("fangkedong@buaa.edu.cn");
    driver.findElement(By.cssSelector("#register_form4 > div.el-form-item__content > div.el-input > input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("#register_form4 > div.el-form-item__content > div.el-input > input.el-input__inner")).sendKeys("123456789");
    driver.findElement(By.cssSelector("#register_form5 > div.el-form-item__content > div.el-input > input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("#register_form5 > div.el-form-item__content > div.el-input > input.el-input__inner")).sendKeys("123456789");
    driver.findElement(By.cssSelector("div.el-dialog.el-dialog--small > div.el-dialog__footer > span.dialog-footer > button.el-button.el-button--primary")).click();
    assertEquals("用户名或邮箱已被注册", closeAlertAndGetItsText());
    driver.findElement(By.cssSelector("input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("input.el-input__inner")).sendKeys("fkdfkd");
    driver.findElement(By.cssSelector("div.el-dialog.el-dialog--small > div.el-dialog__footer > span.dialog-footer > button.el-button.el-button--primary")).click();
    assertEquals("用户名或邮箱已被注册", closeAlertAndGetItsText());
    driver.findElement(By.cssSelector("input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("input.el-input__inner")).sendKeys("fangkedong@10.2.28.124");
    driver.findElement(By.cssSelector("div.el-dialog.el-dialog--small > div.el-dialog__footer > span.dialog-footer > button.el-button.el-button--primary")).click();
    driver.findElement(By.cssSelector("input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("input.el-input__inner")).sendKeys("fkd15061188");
    driver.findElement(By.cssSelector("div.el-dialog.el-dialog--small > div.el-dialog__footer")).click();
    driver.findElement(By.cssSelector("div.el-dialog.el-dialog--small > div.el-dialog__footer > span.dialog-footer > button.el-button.el-button--primary")).click();
    assertEquals("用户名或邮箱已被注册", closeAlertAndGetItsText());
    driver.findElement(By.cssSelector("#register_form6 > div.el-form-item__content > div.el-input > input.el-input__inner")).clear();
    driver.findElement(By.cssSelector("#register_form6 > div.el-form-item__content > div.el-input > input.el-input__inner")).sendKeys("15061188@buaa.edu.cn");
    driver.findElement(By.cssSelector("div.el-dialog.el-dialog--small > div.el-dialog__footer > span.dialog-footer > button.el-button.el-button--primary")).click();
    assertEquals("用户名或邮箱已被注册", closeAlertAndGetItsText());
  }

  @After
  public void tearDown() throws Exception {
    
  }

  private boolean isElementPresent(By by) {
    try {
      driver.findElement(by);
      return true;
    } catch (NoSuchElementException e) {
      return false;
    }
  }

  private boolean isAlertPresent() {
    try {
      driver.switchTo().alert();
      return true;
    } catch (NoAlertPresentException e) {
      return false;
    }
  }

  @SuppressWarnings("finally")
private String closeAlertAndGetItsText() {
	  WebDriverWait wait = new WebDriverWait(driver, 10);
	  Alert alert=null;
      try {
           alert= wait.until(new ExpectedCondition<Alert>() {
              @Override
              public Alert apply(WebDriver driver) {
                  try {
                      return driver.switchTo().alert();
                  } catch (NoAlertPresentException e) {
                      return null;
                  }
              }
          });
          String alertText = alert.getText();
          if (acceptNextAlert) {
            alert.accept();
          } else {
            alert.dismiss();
          }
          return alertText;
      } catch (NullPointerException e) {
      } finally {
          acceptNextAlert = true;   
      }
      return alert.getText();
  }
}