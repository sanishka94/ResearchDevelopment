import { TestBed } from '@angular/core/testing';

import { EamilService } from './eamil.service';

describe('EamilService', () => {
  let service: EamilService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EamilService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
